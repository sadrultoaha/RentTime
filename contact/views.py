from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView, TemplateView
from django.conf import settings
from app.models import User
from .forms import ContactForm
from django.urls import reverse_lazy


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def get_context_data(self, *args, **kwargs):
        curuser = self.request.resolver_match.captured_kwargs['cur_user']
        context = super().get_context_data(**kwargs)

        context.update(
            cur_user =  User.objects.get(username=curuser) #get_object_or_404(User).filter(username=curuser)
        )
        return context


    def form_valid(self, form):
        # Calls the custom send method
        if self.request.method == 'POST':
            curuser = self.request.resolver_match.captured_kwargs['cur_user']
            cur_user =  User.objects.get(username=curuser) 

            form = ContactForm(self.request.POST)
            if form.is_valid():
                settings.RECIPIENT_ADDRESS = cur_user.email
                settings.EMAIL_SENDER_INFO = "From: " + cur_user.first_name +" "+ cur_user.last_name + "\n"
                form.send()
                messages.success(self.request, 'Your message has been sent successfully.')
                return redirect('contact', cur_user)
        else:

            form = ContactForm()
