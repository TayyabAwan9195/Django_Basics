from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utils import send_email_to_client

def home(request):
    peoples=[
        {'name':'Tayyab','age':22},
        {'name':'Faizan Rasool','age':23},
        {'name':'Ehtisham','age':24},
        {'name':'Daniyal','age':30}
    ]
    vegetables=['tomato','pumpkin','potato']
    return render(request,"index.html",context={'page':'Home','peoples':peoples,'vegetables':vegetables})
def about(request):
    context = {'page':'About'}
    return render(request,"about.html",context)
def contact(request):
    context = {'page':'Contact'}
    return render(request,"contact.html",context)


def success_page(request):
    context = {'page':'Success'}
    return HttpResponse(" This is a success page",context)
def send_email(request):
    send_email_to_client()
    return HttpResponse("Message sent !!!! :)")