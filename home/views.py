from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponseRedirect

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home/index.html'


def email_sender(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        subject='Message From Website User'
        text_content='Name: ' + name + '<br>' + 'Email: ' + email + '<br>' + 'Phone: ' + phone + '<br>' + 'Message: ' + message
        html_content='Name: ' + name + '<br>' + 'Email: ' + email + '<br>' + 'Phone: ' + phone + '<br>' + 'Message: ' + message
        from_email='hello@roumpiniresource.com'
        to=['fbilesanmi@gmail.com', 'larnorm@gmail.com']

        email_message = EmailMultiAlternatives(subject, text_content, from_email, to)
        email_message.attach_alternative(html_content, 'text/html')
        email_message.send()
        return redirect('home')
