# Generated by Django 4.2.1 on 2023-05-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_availablebus_added_by_alter_availablebus_bus'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='listed',
            field=models.BooleanField(default=False),
        ),
    ]
