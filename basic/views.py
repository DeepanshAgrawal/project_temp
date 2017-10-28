from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
import datetime
from django.db.models import Q
# author book album song news message Feedback music movie

def srch(q):
    q = str(q).upper()
    r = []
    for i in Thing.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i.tag)
    for i in author.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i.tag)
    for i in book.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i.tag)
    for i in album.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i.tag)
    for i in news.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i.tag)
    for i in message.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i.tag)
    for i in music.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i.tag)
    for i in movie.objects.all():
        if str(i.tag).upper().find(q) is not -1:
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

def addobject(request):
    if request.path == '/basic/addmusic/':
        if request.method =='POST':
            form=MusicForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('basic:index')
        else:
            form=MusicForm()
            return render(request, 'addmusic_html.html', context={'form': form})
    elif request.path == '/basic/addmovie/':
        if request.method =='POST':
            form=MovieForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('basic:index')
        else:
            form=MovieForm()
            return render(request,'addmovie_html.html',context={'form':form})
    elif request.path == '/basic/message/':
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                mess = message()
                mess.sender = request.user
                mess.reciever = form.cleaned_data['reciever']
                mess.message_text = form.cleaned_data['message_text']
                mess.message_date = datetime.datetime.now()
                mess.save()
                return redirect('basic:index')
        else:
            form = MessageForm()
            form.fields['reciever'].queryset = CustomUser.objects.filter(~Q(usr=request.user))
            return render(request, 'startbootstrap-agency-gh-pages/popup.html', { 'form' : form})

def inbox(request):
    r = []
    for i in message.objects.all():
        if str(i.reciever) == str(request.user):
            r.append(i)
    return render(request, 'startbootstrap-agency-gh-pages/inbox.html', { 'message': r})
