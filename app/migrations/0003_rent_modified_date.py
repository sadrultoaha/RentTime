# Generated by Django 4.1.1 on 2022-09-27 20:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_rent_renter'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
