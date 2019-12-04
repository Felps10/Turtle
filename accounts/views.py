from django.shortcuts import render, redirect

# IMPORT DJANGO AUTH
from django.contrib import auth

# IMPORT DJANGO USER MODEL
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check if username exists
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'That username has already been registered. Please try a different username'})
            else:
                # Check if email exists
                if User.objects.filter(email=email).exists():
                    return render(request, 'register.html', {'error': 'That email has already been registered'})
                else:
                    # Register User
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('landing')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        username_form = request.POST['username']
        password_form = request.POST['password']
        #authentication
        user = auth.authenticate(username=username_form, password=password_form)

        if user is not None:
            #login
            auth.login(request,user)
            #redirect
            return redirect('landing')
        else:
            context = {'error':'Invalid Credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

    
def logout(request):
    auth.logout(request)
    return redirect('landing')