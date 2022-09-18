from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView
from ..models import *

def home(request):
    rents = Rent.objects.order_by('-created_date')

    # thana = postoffice.objects.select_related('Thana')
    # division = thana.objects.select_related('Division')
    # district = division.objects.select_related('District')

    return render(request, 'home.html', {'rents': rents})

def about(request):
        return render(request, 'about.html')

class SignUpView(TemplateView):
    template_name = 'signup.html'
         


		