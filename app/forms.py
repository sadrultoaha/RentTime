from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from app.models import *
from django.utils import timezone

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ('address','post_office','availability_date', 'description')
        widgets = {
            'availability_date' : DatePickerInput(attrs={'style': 'width: 300px;', 'class': 'form-control' }),
            'address': forms.TextInput(attrs={'style': 'width: 500px;' , 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'style': 'width: 600px;' , 'class': 'form-control'}),
            'post_office':forms.Select(attrs={'style': 'width: 300px;' , 'class': 'form-control'})
        }

    def __str__(self):
        return self.owner

class RenterChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'nid','email','first_name','last_name','mobile_No')


class OwnerChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'nid','email','first_name','last_name','mobile_No')


class OwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'nid','email','first_name','last_name','mobile_No')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        if commit:
            user.save()
        return user


class RenterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'nid','email','first_name','last_name','mobile_No')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_renter = True
        if commit:
            user.save()
        return user
