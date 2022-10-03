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
    path('rents/details/<pk>/', rents.details, name='details'),
    path('rents/details/<int:pk>/edit/', rents.rent_edit, name='rent_edit'),
    path('rents/add-request/<int:pk>/', rents.add_rent_request, name='add_rent_request'),
    path('rents/delete_request/<int:pk>/', rents.delete_rent_request, name='delete_rent_request'),
    path('rents/accept_request/<int:pk>/', rents.accept_rent_request, name='accept_rent_request'),
    path('rents/add_roommate_status/<int:pk>/', rents.add_roommate_status, name='add_roommate_status'),

    #path('<user>/list/',renters.list, name='list'),
    #path('update/',renters.update),
    #path('programmers/',renters.Programmers,name='Programmers'),

    #path('profile/<user>/',renters.ProgrammersProfile, name='ProgrammersProfile'),
    #path('<user>/profile_edit/',renters.ProgrammersProfile_edit, name='ProgrammersProfile_edit'),
    #path('<user>/profile_edit/Password/',renters.ProgrammersPassword.as_view(), name='ProgrammersPassword'),
    #path('owners/',renters.owner,name='owners'),
    #path('owner/profile/<user>/',owners.ownersProfile, name='ownersProfile'),
    #path('owner/<user>/profile_edit/',owners.ownersProfile_edit, name='ownersProfile_edit'),
    #path('owner/<user>/profile_edit/Password/',owners.ownersPassword.as_view(), name='ownersPassword'),

    # path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='ProgrammersProfile'),
    # path('renters/',renters.ProgrammersProfile, name='ProgrammersProfile'),
    # path('owners/ownersProfile/',TemplateView.as_view(template_name='registration/profile.html'), name='ownersProfile'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
