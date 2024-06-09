from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact
import os
import mimetypes
from django.conf import settings
from django.http import HttpResponse, Http404
from twilio.rest import Client


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



def send_msg(name, subject, email, message):
    print('msg server initiated')

    account_sid = ''
    auth_token = ''
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"You got a message from {name}.\n"
                 f"subject: {subject}. \n"
                 f"email: {email}. \n"
                 f"message: {message}.\n",
            from_='+19898502083',
            to='+919900942125'
        )
        print('ms', message)
        print('*************msg******',message.sid)
        return message.sid
    except Exception as e:
        error = str(e)
        return error




def json_response(request):
    print("json request is received")

    if request.method == 'POST':
        print(request.POST)
        contact = Contact()
        name = request.POST.get('name', None)
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            Contact.objects.create(name=name, subject=subject, email=email, message=message)
            # send_msg(name, subject, email, message)
            status = "success"
        except Exception as e:
            status = str(e)
        finally:
            return JsonResponse({"status": status})

    return JsonResponse({"status":"unknown"})



