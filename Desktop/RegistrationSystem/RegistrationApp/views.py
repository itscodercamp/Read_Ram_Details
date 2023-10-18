from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user
    user_name = user.username
    return render(request, 'index.html', {'user_name': user_name})

def logout(request):
    user = request.user
    if user in request.session:
        del request.session.username
    return HttpResponse("logout")

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

@csrf_exempt
def signup_check(request):
    if  request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Number = request.POST.get('number')
        Password = request.POST.get('password')
        ConfirmPassword = request.POST.get('confirm_password')
        Username = Name+Email
        # if Password == ConfirmPassword:
        #     if User.objects.filter(email = Email).exists():
        #         return HttpResponse('Email already Exists try another one')
        #     else:
        #         user = User.objects.create_user(username=Username,first_name=Name,email=Email,password=Password)
        #         user.set_password(Password)
        #         user.save()
        #         # Authenticate the user and create a session
        #         user = authenticate(request, email=Email, password=Password)
        #         if user is not None:
        #             login( user)  # Create a session for the user

        #         return redirect('home')
        if Password == ConfirmPassword:
            if Registration.objects.filter(Email=Email).exists():
                return JsonResponse({'error': f'This {Email} Email already exists in the database.'})
            if Registration.objects.filter(Number=Number).exists():
                return JsonResponse({'error': f'This {Number} Number already exists in the database.'})
        else:
            users_session = request.session
            user = Registration.objects.create_user(username=Username,first_name=Name,email=Email,password=Password)
            user.set_password(Password)
            user.save()
            return HttpResponse('Successfully Registration')


@csrf_exempt
def login_check(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
    return HttpResponse('success')