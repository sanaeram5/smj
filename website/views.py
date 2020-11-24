from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def projects(request):
    return render(request,'website/projects.html')

def service(request):
    return render(request,'website/service.html')

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        message_phone =request.POST['message-phone']

        #send email
        send_mail(
            'Message from '+ message_name,
            message_name+" "+message_email+" "+message_phone+" "+message,
            message_email,
            ['info@smje.in'],
        )

        return render(request, 'website/contact.html',{"name":message_name})

    else:
        return render(request,'website/contact.html')