from msilib.schema import CreateFolder

from django.http import HttpRequest, HttpResponseRedirect
from numpy import append

from app.views import owners
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

    rent = get_object_or_404(Rent, id=requested_item.flat.id)
    rent.is_booked = True
    rent.renter = requested_item.renter
    rent.modified_date = timezone.now()
    rent.save()
    Request.objects.filter(flat=requested_item.flat.id).exclude( pk=pk, is_accepted = True).delete()

    return HttpResponseRedirect('/requests/')


def add_roommate_status(request, pk):
    rent = get_object_or_404(Rent, pk=pk)
    rent.is_shared = True
    rent.renter = request.user
    rent.modified_date = timezone.now()
    rent.save()
    return HttpResponseRedirect('/')

def requested_rents(request):
    if request.user.is_owner:
        requests = Request.objects.filter(flat__in = list(Rent.objects.values_list('id', flat=True).filter(owner = request.user)))
    elif request.user.is_superuser:
        requests = list( Request.objects.filter(flat__in = list(Rent.objects.values_list('id', flat=True).filter(owner = request.user))))
        requests.extend( Request.objects.filter(flat__in = list(Rent.objects.values_list('id', flat=True)), renter = request.user))
       
    else:
        requests = Request.objects.filter(flat__in = list(Rent.objects.values_list('id', flat=True)), renter = request.user)
    return render(request, 'requests.html', {'requests': requests})


def added_rents(request):
    rents = Rent.objects.filter( owner = request.user, is_deleted=False, is_booked=False).order_by('-created_date')
    return render(request, 'index.html', {'rents': rents})

def approved_bookings(request):
    requests = Request.objects.filter(flat__in = list(Rent.objects.values_list('id', flat=True)), renter = request.user, is_accepted = True)
    return render(request, 'requests.html', {'requests': requests})

