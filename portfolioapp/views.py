from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    return render(request,"portfolioapp/signup.html")


def index(request):
   
        
  return render(request,'portfolioapp/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if(pass1!=pass2):
            messages.error(request, "Passwords didn't match!!")
            return redirect('home')


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
      
        myuser.save()

        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('signin')


    return render(request,"portfolioapp/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "portfolioapp/index.html",{"fname":fname})
        else:
            messages.error(request, "Invalid Username/Password Credentials!!")
            return redirect('home')


    return render(request,"portfolioapp/signin.html")
    

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
    
    