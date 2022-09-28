from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.views import PasswordContextMixin
from django.views.generic.edit import FormView
from django.contrib.auth import update_session_auth_hash

from django.db.models import Max,Avg
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict

from ..decorators import *
from ..forms import *
from ..models import *



class ProgrammersPassword(PasswordContextMixin,FormView):
    form_class = PasswordChangeForm
    success_url = ('/posts')
    template_name = 'Password.html'
    title = ('Password change')

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


def Programmers(request):

    posts = User.objects.filter().order_by('student_Id').exclude(student_Id__isnull=True)    
    return render(request, 'Renters.html', {'posts': posts})


def RentersProfile(request, user):
        user = User.objects.get(username=user)
        return render(request,'profile.html',{'user': user})

def RentersProfile_edit(request,user):
    user = request.user
    if request.method == 'POST':

        form = RenterChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('RentersProfile',user=user)
    else:
        form = RenterChangeForm(instance=user)
    context = {'form': form}
    return render(request, 'profile_edit.html', context)


class RenterSignUpView(CreateView):
    model = User
    form_class = RenterSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Renter'
        return super().get_context_data(**kwargs)            
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('RentersProfile',user=user)
