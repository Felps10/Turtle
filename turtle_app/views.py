from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing(request):
    return render(request, 'landing.html')
