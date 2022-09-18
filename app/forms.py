# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction
# from app.models import User, Rent, Request


# class RentForm(forms.ModelForm):
#     class Meta:
#         model = Rent
#         fields = ('title', 'text')

#     def __str__(self):
#         return self.author


# class RenterChangeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username','email','first_name','last_name','mobile_No')


# class OwnerChangeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email','first_name','last_name','mobile_No')


# class OwnerSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'email','first_name','last_name','mobile_No')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_owner = True
#         if commit:
#             user.save()
#         return user


# class RenterSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'nid','email','first_name','last_name','mobile_No')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_renter = True
#         if commit:
#             user.save()
#         return user
