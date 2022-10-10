import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import ExpressionWrapper, BooleanField, Q
from django.db.models.functions import Now
from django.utils import timezone


# # Create your models here.
# class Food(models.Model):
#     Export_Status = (
#         ('good', 'green'),
#         ('yellow', 'warning'),
#         ('red', 'expired'),
#     )
#     status_date = models.CharField(max_length=10, choices=Export_Status)
#
#     Food_Type = (
#         ('dairy', 'green'),
#         ('beverages', 'warning'),
#         ('frozen vegetables', 'expired'),
#         ('meat', 'expired'),
#         ('fruits', 'expired'),
#     )
#
#     class Food_Category(models.Model):
#         title = models.CharField(max_length=20)
#
#         def __str__(self):
#             return self.title
#
#     person = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     categories = models.ManyToManyField(Food_Category)
#     descriptions = models.CharField(max_length=512)
#     photos = models.ImageField(blank=True)
#     quantity = models.PositiveIntegerField(null=False, default=0)
#     price = models.FloatField(default=0)
#     expiry_date = models.DateField(blank=True)
#
#     class Meta:
#         verbose_name_plural = 'Food Expiry Tracker'

#

# class TrackExportDateStatus(models.Model):
#     GREEN = 'G'
#     YELLOW = 'Y'
#     RED = 'R'
#
#     STATUS_CHOICES = (
#         (GREEN, 'good'),
#         (YELLOW, 'warning'),
#         (RED, 'red'),
#     )
#     export_status = models.CharField(choices=STATUS_CHOICES)
#
#
# class Users(models.Model):
#     firstName = models.CharField(max_length=100)
#     lastName = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#
#

#
#
# class Item(models.Model):
#     STATUS_CHOICES1 = (
#         ('dairy', 'dairy'),
#         ('beverages', 'beverages'),
#         ('frozen vegetables', 'frozen vegetables'),
#         ('meat', 'meat'),
#         ('fruits', 'fruits'),
#     )
#
#     STATUS_CHOICES2 = (
#         ('7', '7'),
#         ('15', '15'),
#         ('21', '21'),
#         ('30', '30'),
#         ('90', '90'),
#     )
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     title = models.CharField(max_length=512)
#     photos = models.ImageField(upload_to='uploaded_images/', blank=True, null=True)
#     quantity = models.PositiveIntegerField(null=False, default=0)
#     food_type = models.CharField(max_length=100, choices=STATUS_CHOICES1)
#     price = models.FloatField(default=0)
#
#     valid_from = models.DateField()
#     valid_to = models.DateField(choices=STATUS_CHOICES2)
#
#
#     class Meta:
#         verbose_name_plural = "Items"
#
#     # tell django what the message representation should be like
#     def __str__(self):
#         return str(self.title)


class Profile(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return str(self.firstName)


class Item(models.Model):
    STATUS_CHOICES1 = (
        ('dairy', 'dairy'),
        ('beverages', 'beverages'),
        ('frozen vegetables', 'frozen vegetables'),
        ('meat', 'meat'),
        ('fruits', 'fruits'),
    )
    user = models.ForeignKey(Profile, related_name="items", on_delete=models.CASCADE, default=1)
    food_type = models.CharField(max_length=100, choices=STATUS_CHOICES1)
    food_title = models.CharField(max_length=120)
    photos = models.ImageField(upload_to='uploaded_images/')
    price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(null=False, default=0)
    valid_from = models.DateField(auto_now=False, auto_now_add=False)
    valid_to = models.DateField(auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return str(self.food_title)
