from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
from PIL import Image
from matplotlib.pyplot import title
from traitlets import default

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
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    is_renter = models.BooleanField(default = False)
    is_owner = models.BooleanField(default = False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    nid = models.CharField(max_length=13, null=True, blank=True)
    mobile_No = models.CharField(max_length=11, null = False, blank=False)
    affiliation_name = models.CharField(max_length=20, null = True, blank=True)
    affiliation_id = models.CharField(max_length=20, null = True, blank=True)
    dob = models.DateTimeField(null=True,blank=True)
    present_address = models.CharField(max_length=255, blank=True)
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
    rental = models.IntegerField(null = False, default=0)
    is_booked = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_shared = models.BooleanField(default = False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(null = True)
    photo1 = models.ImageField(upload_to='images/', default='images/home.jpg', blank=True)
    photo2 = models.ImageField(upload_to='images/', default='images/home.jpg', blank=True)
    photo3 = models.ImageField(upload_to='images/', default='images/home.jpg', blank=True)

    def __str__(self):
        return str(self.address) + str(': ') + str(self.owner)

    def save(self):
        super().save() 
        img1 = Image.open(self.photo1.path)
        new_img1 = img1.resize((300, 300), resample=Image.ANTIALIAS)
        new_img1.save(self.photo1.path)

        img2 = Image.open(self.photo2.path)
        new_img2 = img2.resize((300, 300), resample=Image.ANTIALIAS)
        new_img2.save(self.photo2.path)

        img3 = Image.open(self.photo3.path)
        new_img3 = img3.resize((300, 300), resample=Image.ANTIALIAS)
        new_img3.save(self.photo3.path)

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


class Blog(models.Model):
    author = models.ForeignKey('User', related_name='blog_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(null = True)
    photo = models.ImageField(upload_to='images/', default='images/home.jpg', blank=True)

    def __str__(self):
        return str(self.id)
