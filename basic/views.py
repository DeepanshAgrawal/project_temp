from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *

def srch(q):
    r = []
    for i in Thing.objects.all():
        if i.tag.find(q) is not -1:
            r.append(i.tag)
    return r

@login_required(login_url='login:login')
def search(request):
    if(request.method == 'POST'):
        result = srch(request.POST['query'])
        return render(request, 'form-search.html', {'get': result, 'value':request.POST['query']})
    else:
        return render(request, 'form-search.html')

@login_required(login_url='login:login')
def home(request):
    for usr in CustomUser.objects.all():
        if str(usr.usr) == str(request.user):
            return render(request, 'startbootstrap-agency-gh-pages/index.html', {'user': usr.usr})
    new = CustomUser(usr=request.user)
    new.save()
    return render(request, 'startbootstrap-agency-gh-pages/index.html', {'user': new})


def logOut(request):
    logout(request)
    return redirect('login:login')

@login_required(login_url='login:login')
def feed(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('basic:index')
    else:
        return render(request, 'startbootstrap-agency-gh-pages/index.html', {'message':'feedback already exists'})


def addmusic(request):
    if request.method =='POST':
        form=MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basic:index')
    else:
        form=MusicForm()
    return render(request,'addmusic_html.html',context={'form':form})

def addmovie(request):
    if request.method =='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basic:index')
    else:
        form=MovieForm()
        return render(request,'addmovie_html.html',context={'form':form})

