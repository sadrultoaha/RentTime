# Generated by Django 4.1.1 on 2022-09-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rent_modified_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='affiliation_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='affiliation_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='present_address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
