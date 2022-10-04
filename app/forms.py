from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from app.models import *
from django.utils import timezone
from django.contrib.auth.models import Group


class DatePickerInput(forms.DateInput):
    input_type = 'date'

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ('address','post_office','availability_date', 'description', 'photo')
        widgets = {
            'availability_date' : DatePickerInput(attrs={'style': 'width: 300px;', 'class': 'form-control' }),
            'address': forms.TextInput(attrs={'style': 'width: 500px;' , 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'style': 'width: 600px;' , 'class': 'form-control'}),
            'post_office':forms.Select(attrs={'style': 'width: 300px;' , 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*;capture=camera'})
        }

    def __str__(self):
        return self.owner


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'photo')
        # widgets = {
        #     'title': forms.TextInput(attrs={'style': 'width: 500px;' , 'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'style': 'width: 600px;' , 'class': 'form-control'}),
        #     'photo': forms.FileInput(attrs={'accept': 'image/*;capture=camera'})
        # }

    def __str__(self):
        return self.title

class RenterChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','nid','email','first_name','last_name','mobile_No','affiliation_name', 'affiliation_id', 'dob', 'present_address')
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username','required':'True' }),
            'nid': forms.TextInput(attrs={'placeholder': 'Nid', 'required':'False'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required':'True'}),
            'first_name':forms.TextInput(attrs={'placeholder': 'First Name', 'required':'True'}),
            'last_name':forms.TextInput(attrs={'placeholder': 'Last Name', 'required':'False'}),
            'mobile_No':forms.TextInput(attrs={'placeholder': 'Mobile No', 'required':'True'}),
            'affiliation_name':forms.TextInput(attrs={'placeholder': 'Institute Name', 'required':'False'}),
            'affiliation_id':forms.TextInput(attrs={'placeholder': 'Your Institutional Id', 'required':'False'}),
            'dob': DatePickerInput(attrs={'placeholder': 'Date of Birth', 'required':'True'}),
            'present_address':forms.TextInput(attrs={'placeholder': 'Present Address', 'required':'True'})
        }

class OwnerChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','nid','email','first_name','last_name','mobile_No','affiliation_name', 'affiliation_id', 'dob', 'present_address')
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username','required':'True' }),
            'nid': forms.TextInput(attrs={'placeholder': 'Nid', 'required':'False'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required':'True'}),
            'first_name':forms.TextInput(attrs={'placeholder': 'First Name', 'required':'True'}),
            'last_name':forms.TextInput(attrs={'placeholder': 'Last Name', 'required':'False'}),
            'mobile_No':forms.TextInput(attrs={'placeholder': 'Mobile No', 'required':'True'}),
            'affiliation_name':forms.TextInput(attrs={'placeholder': 'Institute Name', 'required':'False'}),
            'affiliation_id':forms.TextInput(attrs={'placeholder': 'Your Institutional Id', 'required':'False'}),
            'dob': DatePickerInput(attrs={'placeholder': 'Date of Birth', 'required':'True'}),
            'present_address':forms.TextInput(attrs={'placeholder': 'Present Address', 'required':'True'})
        }

class OwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','first_name','last_name','password1', 'password2', 'photo')
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username','required':'True', 'class': 'input-field' }),
            #'nid': forms.TextInput(attrs={'placeholder': 'Nid', 'required':'False', 'class': 'input-field'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required':'True', 'class': 'input-field'}),
            'first_name':forms.TextInput(attrs={'placeholder': 'First Name', 'required':'True', 'class': 'name-field'}),
            'last_name':forms.TextInput(attrs={'placeholder': 'Last Name', 'required':'False', 'class': 'name-field'}),
            #'mobile_No':forms.TextInput(attrs={'placeholder': 'Mobile No', 'required':'True', 'class': 'input-field'}),
            #'affiliation_name':forms.TextInput(attrs={'placeholder': 'Institute Name', 'required':'False', 'class': 'input-field'}),
            #'affiliation_id':forms.TextInput(attrs={'placeholder': 'Your Institutional Id', 'required':'False', 'class': 'input-field'}),
            #'dob': DatePickerInput(attrs={'placeholder': 'Date of Birth', 'required':'True', 'class': 'input-field'}),
            #'present_address':forms.TextInput(attrs={'placeholder': 'Present Address', 'required':'True', 'class': 'input-field'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*;capture=camera'})
        }
        
    def save(self, commit=True):
        user = super().save(commit='False')
        user.is_owner = True
        if commit:
            user.save()
        return user


class RenterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','first_name','last_name','password1', 'password2', 'photo')

        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username','required':'True', 'class': 'input-field' }),
            #'nid': forms.TextInput(attrs={'placeholder': 'Nid', 'required':'False', 'class': 'input-field'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required':'True', 'class': 'input-field'}),
            'first_name':forms.TextInput(attrs={'placeholder': 'First Name', 'required':'True', 'class': 'name-field'}),
            'last_name':forms.TextInput(attrs={'placeholder': 'Last Name', 'required':'False', 'class': 'name-field'}),
            #'mobile_No':forms.TextInput(attrs={'placeholder': 'Mobile No', 'required':'True', 'class': 'input-field'}),
            #'affiliation_name':forms.TextInput(attrs={'placeholder': 'Institute Name', 'required':'False', 'class': 'input-field'}),
            #'affiliation_id':forms.TextInput(attrs={'placeholder': 'Your Institutional Id', 'required':'False', 'class': 'input-field'}),
            #'dob': DatePickerInput(attrs={'placeholder': 'Date of Birth', 'required':'True', 'class': 'input-field'}),
            #'present_address':forms.TextInput(attrs={'placeholder': 'Present Address', 'required':'True', 'class': 'input-field'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*;capture=camera'})
        }
            
    def save(self, commit=True):
        user = super().save(commit='False')
        renter_group = Group.objects.get(name='renter') 
        user.groups.add(renter_group)
        user.is_renter = True
        if commit:
            user.save()
        return user
