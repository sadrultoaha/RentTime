from msilib.schema import CreateFolder

from django.http import HttpResponseRedirect
from ..models import *
from ..forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def index(request, option):
    if(str(option).lower() == "shared"):
        rents = Rent.objects.filter(is_shared=True, is_deleted=False, is_booked=False).order_by('-created_date')
    else:
        rents = Rent.objects.filter(is_shared=False, is_deleted=False, is_booked=False).order_by('-created_date')

    return render(request, 'index.html', {'rents': rents})


def details(request, pk):
    rent = get_object_or_404(Rent, pk=pk)
    return render(request, 'rent-details.html', {'rent': rent})

def rent_new(request):
    if request.method == "POST":
        form = RentForm(request.POST, request.FILES)
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
    if request.method == "POST":
        form = RentForm(request.POST, request.FILES, instance=rent)
        if form.is_valid():
            rent = form.save(commit=False)
            rent.owner = request.user
            rent.modified_date = timezone.now()
            rent.save()
            return redirect('details', pk=rent.pk)
    else:
        form = RentForm(instance=rent)
    return render(request, 'rent-edit.html', {'form': form, 'req':request})


def add_rent_request(request, pk):
    requested_flat = get_object_or_404(Rent, pk=pk)
    requested_by = request.user
    rent_req = Request(
        flat = requested_flat,
        renter = requested_by,
        is_roommate = requested_flat.is_shared)
    rent_req.save()
    return HttpResponseRedirect('/')

def delete_rent_request(request, pk):
    requested_item = get_object_or_404(Request, pk=pk)
    requested_item.delete()
    return HttpResponseRedirect('/')

def accept_rent_request(request, pk):
    requested_item = get_object_or_404(Request, pk=pk)
    requested_item.is_accepted = True
    requested_item.modified_date = timezone.now()
    requested_item.save()
    print(requested_item.flat)
    print(requested_item.flat.id)
    rent = get_object_or_404(Rent, id=requested_item.flat.id)
    rent.is_booked = True
    rent.renter = requested_item.renter
    rent.modified_date = timezone.now()
    rent.save()
    return HttpResponseRedirect('/')


def add_roommate_status(request, pk):
    rent = get_object_or_404(Rent, pk=pk)
    rent.is_shared = True
    rent.renter = request.user
    rent.modified_date = timezone.now()
    rent.save()
    return HttpResponseRedirect('/')

    


