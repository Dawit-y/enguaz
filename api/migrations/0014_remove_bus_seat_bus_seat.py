# Generated by Django 4.2.1 on 2023-06-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_bus_seat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='seat',
        ),
        migrations.AddField(
            model_name='bus',
            name='seat',
            field=models.ManyToManyField(to='api.seat'),
        ),
    ]
