from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):

    subject = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self, **kwargs):
        """
        Method that returns formatted information
        :return: subject, msg
        """

        # Cleaned data
        cl_data = super().clean()
        subject = " RentApp: " + cl_data.get('subject')
        msg = cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()
        send_mail(
            subject=subject,
            message= settings.EMAIL_SENDER_INFO  + "message : \n" + msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )