from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

def index(request):
    return redirect('/shows')

def shows(request):
    context={
        'all_shows': Show.objects.all()
    }
    return render(request, "shows.html", context)

def create(request):
    if request.method=="GET":
        return render(request, 'new.html')
    else:
        errors = Show.objects.addShowValidation(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            context = {
                'title': request.POST['title'],
                'network': request.POST['network'],
                'release_date': request.POST['release_date'],
                'description': request.POST['description']
            }
            return render(request, 'new.html', context)
        show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect(f'/shows/{show.id}')

def display(request, show_id):
    context={
        'tv_show': Show.objects.get(id=show_id)
    }
    return render(request, 'display.html', context)

def update(request, show_id):
    if request.method=="GET":
        context={
            'tv_show': Show.objects.get(id=show_id)
        }
        return render(request, 'edit.html', context)
    else:
        show = Show.objects.get(id=show_id)
        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.description=request.POST['description']
        errors = Show.objects.addShowValidation(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            context = {
                'tv_show': show
            }
            return render(request, 'edit.html', context)
        show.save()
        context={
            'tv_show': show
        }
    return render(request, 'display.html', context)

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    print(show.title)
    show.delete()
    return redirect('/shows')