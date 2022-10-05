from django.urls import include, path
from .views import rentapp, renters, owners, rents
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', rentapp.home, name='home'),
    path('about/', rentapp.about, name='about'),
    path('rents/new/', rents.rent_new, name='rent_new'),
    path('rents/<option>/', rents.index, name='index'),
    path('rents/details/<int:pk>/', rents.details, name='rent_details'),
    path('rents/delete/<int:pk>/', rents.delete, name='rent_delete'),
    path('rents/details/<int:pk>/edit/', rents.rent_edit, name='rent_edit'),

    path('rents/add-request/<int:pk>/', rents.add_rent_request, name='add_rent_request'),
    path('rents/delete_request/<int:pk>/', rents.delete_rent_request, name='delete_rent_request'),
    path('rents/accept_request/<int:pk>/', rents.accept_rent_request, name='accept_rent_request'),
    path('rents/add_roommate_status/<int:pk>/', rents.add_roommate_status, name='add_roommate_status'),

    path('requests/', rents.requested_rents, name='requests'),
    path('listings/', rents.added_rents, name='added_rents'),
    path('approvals/', rents.approved_bookings, name='approved_bookings'),

    path('blogs/', rentapp.blogs, name='blogs'),
    path('myblogs/', rentapp.my_blogs, name='my_blogs'),
    path('blogs/new/', rentapp.blog_new, name='blogs_new'),
    path('blogs/details/<int:pk>/', rentapp.blog_details, name='blog_details'),
    path('blogs/delete/<int:pk>/', rentapp.blog_delete, name='blog_delete'),
    path('blogs/details/<int:pk>/edit/', rentapp.blog_edit, name='blog_edit'),


    path('profile/<user>/',renters.RentersProfile, name='renters_profile'),
    path('profile_edit/',renters.RentersProfile_edit, name='renters_profile_edit'),
    path('profile_edit/password/',renters.RentersPassword.as_view(), name='renters_password'),

    #path('owners/',renters.owner,name='owners'),
    #path('owner/profile/<user>/',owners.ownersProfile, name='ownersProfile'),
    #path('owner/<user>/profile_edit/',owners.ownersProfile_edit, name='ownersProfile_edit'),
    #path('owner/<user>/profile_edit/Password/',owners.ownersPassword.as_view(), name='ownersPassword'),

    # path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='ProgrammersProfile'),
    # path('renters/',renters.ProgrammersProfile, name='ProgrammersProfile'),
    # path('owners/ownersProfile/',TemplateView.as_view(template_name='registration/profile.html'), name='ownersProfile'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
