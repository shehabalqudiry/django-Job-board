from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    info = Info.objects.first()
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        subject = request.POST['subject']
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
    context = {'info':info}
    return render(request, 'contact/contact.html', context)