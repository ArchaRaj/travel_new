from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from travel_app.models import Place,Place2


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Place2.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})

def register(request):
    if request.method=='POST':
        username=request.POST['uname']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['mail']
        password=request.POST['pass']
        cpassword=request.POST['cpass']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                u=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                u.save()
                print("User registered")

                return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
    return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname1']
        password = request.POST['pass1']
        user = auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')