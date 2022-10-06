from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from ..filters import *
from ..models import *
from ..forms import *
from django.utils import timezone

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
		