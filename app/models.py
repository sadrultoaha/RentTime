from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
from PIL import Image

class Division(models.Model):
    code = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    is_deleted = models.BooleanField(default = False)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('User', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class District(models.Model):
    code = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    division = models.ForeignKey('Division', related_name = 'district_division', on_delete= models.CASCADE)
    is_deleted = models.BooleanField(default = False)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('User', related_name = 'created_by', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Thana(models.Model):
    code = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    district = models.ForeignKey('District', related_name = 'thana_district', on_delete= models.CASCADE)
    is_deleted = models.BooleanField(default = False)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('User', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class PostOffice(models.Model):
    code = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    thana = models.ForeignKey('Thana', related_name = 'postoffice_thana', on_delete= models.CASCADE)
    is_deleted = models.BooleanField(default = False)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('User', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_renter = models.BooleanField(default = False)
    is_owner = models.BooleanField(default = False)
    nid = models.CharField(max_length=13, null = True)
    mobile_No = models.CharField(max_length=11, null = True)
    affiliation_name = models.CharField(max_length=20, null = True)
    affiliation_id = models.CharField(max_length=20, null = True)
    dob = models.DateTimeField(null = True)
    present_address = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to='images/', default='images/user.jpg', blank=True)

    def __str__(self):
        return self.username

class Rent(models.Model):
    owner = models.ForeignKey('User', related_name='rent_owner', on_delete=models.CASCADE)
    renter = models.ForeignKey('User', related_name='rent_renter', blank=True, null=True, on_delete=models.CASCADE)
    post_office = models.ForeignKey('PostOffice', related_name = 'address_postoffice', on_delete= models.CASCADE)
    address = models.CharField(max_length = 255, null=False)
    description = models.TextField()
    availability_date = models.DateTimeField(null = False)
    is_booked = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_shared = models.BooleanField(default = False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(null = True)
    photo = models.ImageField(upload_to='images/', default='images/home.jpg', blank=True)

    def __str__(self):
        return str(self.id)

    def save(self):
        super().save() 
        img = Image.open(self.photo.path)
        new_img = img.resize((300, 300), resample=Image.ANTIALIAS)
        new_img.save(self.photo.path)

class Request(models.Model):
    flat = models.ForeignKey('Rent', related_name='requested_rent', on_delete=models.CASCADE)
    renter = models.ForeignKey('User', related_name='requested_by', on_delete=models.CASCADE)
    is_roommate = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateField(null = True)

    def __str__(self):
        return str(self.id)

