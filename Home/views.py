from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.
def homepage(request):
    print('hi there')
    return render(request, "index.html")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'Akash Kantrikar - Resume.pdf')
    print('file_path', file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("main:homepage")

    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})