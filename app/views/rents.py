from django.shortcuts import render
from ..models import *
from ..forms import *
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def index(request, option):
    rents = Rent.objects.filter(is_shared=option).order_by('-created_date')
    by = Rent.objects.all        
    return render(request, 'index.html', {'rents': rents,'by':by})


# def details(request,pk):
#     rent = get_object_or_404(Rent, pk=pk)
#     return render(request, 'details.html', {'rent': rent})


# def rent_new(request):
#     if request.method == "rent":
#         form = rentForm(request.rent)
#         if form.is_valid():
#             rent = form.save(commit=False)
#             rent.author = request.user
#             rent.published_date = timezone.now()
#             rent.save()
#             return redirect('details', pk=rent.pk)
#     else:
#         form = rentForm()
#     return render(request, 'rent_edit.html', {'form': form})

# def rent_edit(request, pk):
#     rent = get_object_or_404(rents, pk=pk)

#     if request.method == "rent":
#         form = rentForm(request.rent, instance=rent)
#         if form.is_valid():
#             rent = form.save(commit=False)
#             rent.author = request.user
#             rent.published_date = timezone.now()
#             rent.save() 
#             return redirect('details', pk=rent.pk)
#     else:
#         form = rentForm(instance=rent)
#     return render(request, 'rent_edit.html', {'form': form})

# def contest(request):
#     rents = rents.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     by = rents.objects.all        
#     return render(request, 'contest.html', {'rents': rents,'by':by})


# def condetails(request,pk):
#     rent = get_object_or_404(rents, pk=pk)
#     return render(request, 'condetails.html', {'rent': rent})


# def con_new(request):
#     if request.method == "rent":
#         form = ContestForm(request.rent)
#         if form.is_valid():
#             rent = form.save(commit=False)
#             rent.publisher = request.user
#             rent.save()
#             return redirect('details', pk=rent.pk)
#     else:
#         form = ContestForm()
#     return render(request, 'con_new.html', {'form': form})

# def con_edit(request, pk):
#     rent = get_object_or_404(Contests, pk=pk)

#     if request.method == "rent":
#         form = ContestForm(request.rent, instance=rent)
#         if form.is_valid():
#             rent = form.save(commit=False)
#             rent.publisher = request.user
#             rent.save() 
#             return redirect('details', pk=rent.pk)
#     else:
#         form = ContestForm(instance=rent)
#     return render(request, 'con_new.html', {'form': form}) 


