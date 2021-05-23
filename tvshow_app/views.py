from django.shortcuts import render, redirect
from .models import *

def index(request):
    context={
        'testing': 'Initial TV SHOW project is working!!!'
    }
    return render(request, "index.html", context)
