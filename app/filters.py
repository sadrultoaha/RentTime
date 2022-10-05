import django_filters
from .models import *
from django_filters import CharFilter
from django import forms

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class RentFilter(django_filters.FilterSet):
    address = CharFilter(field_name="address", lookup_expr='icontains') #widget=forms.TextInput(attrs={"class":"form-control text-white text-center","max_length":"100"})
    rental = django_filters.NumberFilter()
    rental__gte = django_filters.NumberFilter(field_name='rental', lookup_expr='gte')
    rental__lte = django_filters.NumberFilter(field_name='rental', lookup_expr='lte')
    class Meta:
        model = Rent
        fields = ['post_office','address','rental']
        
