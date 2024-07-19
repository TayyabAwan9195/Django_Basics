from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# This is a decorator which ensure user to access reciepes page after login  
@login_required(login_url="/login/") 
def reciepes(request):
    if request.method == "POST":
        data=request.POST

        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_image=receipe_image,
            receipe_description=receipe_description,
             )
        return redirect('/reciepes/')
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context={'reciepes':queryset}
   
    return render(request,"receipes.html",context)


def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/reciepes/')

    context={'receipe':queryset} 
    return render(request,"update_receipes.html",context)


def delete_receipe(request,id):
    queryset=Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/reciepes/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/login/')
        user = authenticate(username = username,password = password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/reciepes/')        
    return render(request,"login.html")


def log_out(request):
    logout(request)
    return redirect('/login/')


def register_page(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username Already Exist')
            return redirect('/register/')
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account Created')

        return redirect('/register/')
    


    return render(request,"register.html")


