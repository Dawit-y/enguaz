# Generated by Django 4.2.1 on 2023-06-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_bus_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='bus',
            name='station',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='station',
        ),
    ]
