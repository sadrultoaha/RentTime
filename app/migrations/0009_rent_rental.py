# Generated by Django 4.1.1 on 2022-10-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='rental',
            field=models.IntegerField(default=0),
        ),
    ]
