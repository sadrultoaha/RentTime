from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView
from ..models import *

def home(request):
    rents = Rent.objects.filter(is_deleted=False, is_booked=False).order_by('-created_date')
    return render(request, 'home.html', {'rents': rents})

def about(request):
        return render(request, 'about.html')



		