from django.shortcuts import render, redirect # type: ignore
from .models import User
from django.contrib import messages, auth # type: ignore
from django.contrib.auth import login, logout, authenticate # type: ignore
# Create your views here.

def signup(request): 

    if request.method == "POST": 
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        username =  request.POST['username']
        if password == repeat_password: 
            user = User.objects.create_user(
                first_name = email.split('@')[0],
                last_name = email.split('@')[0],
                email = email,
                username =username,
                password = password

            )
            user.save()
            messages.success(request, 'successfully singup, you can now login')
        
            return redirect('signup')
        
        messages.error(request, 'both passwords must match')

 
    return render(request, 'ecommerce/pages/signup.html')


def Signin(request):
    if request.method == "POST": 
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(
            email = email, 
            password = password

        )
        if user is not None: 
            messages.error(request, 'account with credentials does not exist')
        auth.login(request, user)
        messages.success(request, 'successfully logged in')

    return render(request, 'ecommerce/pages/login.html')

def logout(request): 
    auth.logout(request)
    messages.success(request, 'logged out successfully')

    return redirect('signin')