from django.shortcuts import redirect

def dawn(request):
    return redirect('login:login')