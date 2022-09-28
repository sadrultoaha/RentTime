from ..models import *
from ..forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def index(request, option):
    if(str(option).lower() == "shared"):
        rents = Rent.objects.filter(is_shared=True).order_by('-created_date')
    else:
        rents = Rent.objects.order_by('-created_date')

    return render(request, 'index.html', {'rents': rents})


def details(request,pk):
    rent = get_object_or_404(Rent, pk=pk)
    return render(request, 'rent-details.html', {'rent': rent})


def rent_new(request):
    if request.method == "POST":
        form = RentForm(request.POST)
        if form.is_valid():
            rent = form.save(commit=False)
            rent.owner = request.user
            rent.save()
            return redirect('details', pk=rent.pk)
    else:
        form = RentForm()
    return render(request, 'rent-edit.html', {'form': form, 'req':request})


def rent_edit(request, pk):
    rent = get_object_or_404(Rent, pk=pk)
    print(rent, pk)
    if request.method == "POST":
        form = RentForm(request.POST, instance=rent)
        if form.is_valid():
            rent = form.save(commit=False)
            rent.owner = request.user
            rent.modified_date = timezone.now()
            rent.save()
            return redirect('details', pk=rent.pk)
    else:
        form = RentForm(instance=rent)
    return render(request, 'rent-edit.html', {'form': form, 'req':request})
