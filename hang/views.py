from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from . forms import EnskripsyonForm
# Create your views here.

def akey(request):
    context = {

    }
    return render(request, 'akey.html', context)

def enskripsyon(request):
    if request.method == 'POST':
        form = EnskripsyonForm(data=request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        modpass = request.POST.get('modpass')
        if form.is_valid():
            formEnskripsyon = User.objects.create_user(first_name=first_name, last_name=last_name,
            username=username, modpass=modpass)
            return redirect(akey)
        else:
            print('dezole gen yon detay ki pa korek')
    else:
        form = EnskripsyonForm()
    context = {
        'form' : form,
    }
    return render(request, 'enskripsyon.html', context)

def koneksyon(request):
    context = {

    }
    return render(request, 'koneksyon.html', context)
