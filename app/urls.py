from django.urls import include, path
from .views import rentapp, rents
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


    path('profile/<user>/',rentapp.UserProfile, name='user_profile'),
    path('profile_edit/',rentapp.UserProfile_edit, name='user_profile_edit'),
    path('profile_edit/password/',rentapp.UserPassword.as_view(), name='user_password'),


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
