from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date, time, datetime
from .models import *

def index(request):
    request.session.clear()
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
        errors = Show.objects.showValidation(request.POST, '')
        request.session['title']=request.POST['title']
        request.session['network']=request.POST['network']
        request.session['release_date']=request.POST['release_date']
        request.session['description']=request.POST['description']
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect(f'/shows/{show.id}')

def display(request, show_id):
    show = Show.objects.get(id=show_id)
    request.session['id'] = show.id
    request.session['title'] = show.title
    request.session['network'] = show.network
    request.session['release_date'] = str(show.release_date)
    request.session['description'] = show.description
    return render(request, 'display.html')

def update(request, show_id):
    show = Show.objects.get(id=show_id)
    if request.method=="GET":
        if 'title' not in request.session:
            request.session['id'] = show.id
            request.session['title'] = show.title
            request.session['network'] = show.network
            request.session['release_date'] = str(show.release_date)
            request.session['description'] = show.description
        return render(request, 'edit.html')
    else:
        errors = Show.objects.showValidation(request.POST, show.title)
        request.session['title']=request.POST['title']
        request.session['network']=request.POST['network']
        request.session['release_date']=request.POST['release_date']
        request.session['description']=request.POST['description']
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')
        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.description=request.POST['description']
        show.save()
        request.session.clear()
    return redirect(f'/shows/{show_id}')

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    print(show.title)
    show.delete()
    return redirect('/')