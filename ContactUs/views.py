from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contactus(request):
    contact = ''
    if request.method == 'POST':
        rp = request.POST
        Contact.objects.create_contact(rp['name'],rp['email'],rp['subject'],rp['message'])
        send_mail(
            'Your message was send.',
            f'Hello {rp["name"]}. Your subject: {rp["subject"]}. Your message: {rp["message"]}',
            'shoptest20001@gmail.com',
            [rp['email']],
            fail_silently=False,
        )
        messages.success(request,'Your message is send')
    return render(request, 'ContactUs/contactus.html',{'contact':contact})