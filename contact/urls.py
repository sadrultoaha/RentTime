from django.urls import path
from .views import ContactView

#app_name = 'contact'

urlpatterns = [
    path('contact/<cur_user>/', ContactView.as_view(), name="contact")
]