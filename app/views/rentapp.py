from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from ..filters import *
from ..models import *
from ..forms import *
from django.utils import timezone

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordContextMixin
from django.views.generic.edit import FormView
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone
from django.shortcuts import render

from app.decorators import *
from ..forms import *
from ..models import *


def home(request):
    rents = Rent.objects.filter(is_deleted=False, is_booked=False).order_by('-created_date')    
    myFilter = RentFilter(request.GET, queryset=rents)
    rents = myFilter.qs
    context = {
        'myFilter': myFilter,
        'rents': rents,
    }
    return render(request, 'home.html', context)

def about(request):
        return render(request, 'about.html')

class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'owner_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect('/')

class RenterSignUpView(CreateView):
    model = User
    form_class = RenterSignUpForm
    template_name = 'renter_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'renter'
        return super().get_context_data(**kwargs)            
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect('/')


class UserPassword(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = ('/')
    template_name = 'password-edit.html'
    title = ('Password change')

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)

@login_required
def UserProfile(request, user):
    cur_user =  User.objects.get(username=user)

    if cur_user.is_renter:
        requests = Request.objects.filter(flat__in = list(Rent.objects.values_list('id', flat=True)), renter = cur_user, is_accepted = True)
    else:
        requests = Request.objects.filter(flat__in = list(Rent.objects.values_list('id', flat=True).filter(owner = cur_user)), is_deleted = False, is_accepted = True )

    context={
        'cur_user':cur_user,
        'requests':requests,

    }
    return render(request,'profile.html', context)
        
def UserProfile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = RenterChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_profile', user=user)
    else:
        form = RenterChangeForm(instance=user)
    context = {'user':user,'form': form}
    return render(request, 'profile_edit.html', context)



def blogs(request):
    blogs = Blog.objects.filter(is_deleted=False).order_by('-created_date')
    return render(request, 'blog-page.html', {'blogs': blogs})

def blog_details(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog-details.html', {'blog': blog})

def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_details', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blog-edit.html', {'form': form, 'req': request})

def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.modified_date = timezone.now()
            blog.save()
            return redirect('blog_details', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog-edit.html', {'form': form, 'req':request})


def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk).delete()
    return HttpResponseRedirect('/blogs/')
    
def my_blogs(request):
    blogs = Blog.objects.filter( author = request.user, is_deleted=False).order_by('-created_date')
    return render(request, 'blog-page.html', {'blogs': blogs})
		