from django.contrib.auth.models import User
from django.db import models

from accounts.models import Profile


class Item(models.Model):
    STATUS_CHOICES1 = (
        ('dairy', 'dairy'),
        ('beverages', 'beverages'),
        ('frozen vegetables', 'frozen vegetables'),
        ('meat', 'meat'),
        ('fruits', 'fruits'),
    )

    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
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
