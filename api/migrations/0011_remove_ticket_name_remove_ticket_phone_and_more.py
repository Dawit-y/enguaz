# Generated by Django 4.2.1 on 2023-06-02 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='phone',
        ),
        migrations.AddField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='api.customer'),
            preserve_default=False,
        ),
    ]