# Generated by Django 4.2.1 on 2023-06-03 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_station_remove_bus_station_remove_worker_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='station',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='api.station'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='station',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='api.station'),
            preserve_default=False,
        ),
    ]
