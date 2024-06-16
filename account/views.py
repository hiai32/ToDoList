from django.shortcuts import render, redirect
from account.models import User
from todolist.views import *

# Create your views here.
def login(request):
    errormessage = None

    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        
        try:
            user = User.objects.get(name=name)
            if user.password != password:
                errormessage = 'パスワードが間違っています'
            else:
                return redirect(home, user.id)
        except:
            errormessage = 'このユーザー名は存在しません'
        
    context = {
        'errormessage': errormessage
    }

    return render(request, 'account/login.html', context)

def signup(request):
    errormessage = None

    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if User.objects.filter(password=password).exists():
            errormessage = 'このパスワードは既に使用されています'
        elif password != confirmation:
            errormessage = 'パスワードが一致しません'
        else:
            user = User(name=name, password=password)
            user.save()
            return redirect(login)
        
    context = {
        'errormessage': errormessage
    }

    return render(request, 'account/signup.html', context)
