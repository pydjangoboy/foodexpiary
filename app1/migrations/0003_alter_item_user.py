# Generated by Django 3.2.16 on 2022-10-13 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app1.profile'),
        ),
    ]