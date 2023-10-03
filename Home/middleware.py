from twilio.rest import Client


class SmsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request, *args, **kwargs):
        print(request.method)
        if request.method == 'POST':
            name = request.POST.get('name')
            subject = request.POST.get('Subject')
            email = request.POST.get('email')
            message = request.POST.get('message')
            send_msg(name, subject, email, message)
        response = self.get_response(request)
        return response


def send_msg(name, subject, email, message):

    account_sid = 'some'
    auth_token = 'some'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"You got a message from {name}.\n"
             f"subject: {subject}. \n"
             f"email: {email}. \n"
             f"message: {message}.\n",
        from_='+12407700012',
        to='+919900942125'
    )
    return message.sid


