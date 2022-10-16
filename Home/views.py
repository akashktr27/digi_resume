from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import Contact
import os
import mimetypes
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        subject = request.POST.get('Subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.subject = subject
        contact.email = email
        contact.message = message
        contact.save()
        messages.info(request, 'Your password has been changed successfully!')
    return render(request, "index.html")

def download(request):
    filename = 'Akash Kantrikar - Resume.pdf'
    if filename != '':
        file_path = os.path.join(settings.MEDIA_ROOT, 'Akash Kantrikar - Resume.pdf')
        path = open(file_path, 'rb')
        mime_type, _ = mimetypes.guess_type(file_path)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    raise Http404


