from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def login(requ):
    if requ.method == 'POST':
        username = requ.POST['username']
        password = requ.POST['password']

        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(requ, user)
            messages.add_message(requ, messages.SUCCESS,'Oturum açıldı.')
            return redirect('index')
        else:
            messages.add_message(requ, messages.ERROR, 'Hatalı kullanıcı adı veya parola')
            return redirect('login')
    else:
        return render(requ, 'user/login.html')


def register(req):
    if req.method == 'POST':
        # get form values
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        repassword = req.POST['repassword']

        if password == repassword:
            #Username
            if User.objects.filter(username = username).exists():
                messages.add_message(req, messages.WARNING,
                                     'Bu kullanıcı adı daha önce alınmış.')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(req, messages.WARNING,
                                         'Bu mail adresi daha önce alınmış.')
                    return redirect('register')
                else:
                    #herşey tamam
                    user = User.objects.create_user(username=username,password = password, email = email)
                    user.save()
                    messages.add_message(req, messages.SUCCESS,
                                         'Hesabınız oluşturuldu.')
                    return redirect('login')
            
        else:
            print('Parolalar eşleşmiyor.')
            return redirect('register')
    else:
        return render(req, 'user/register.html')


def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        messages.add_message(req, messages.SUCCESS, 'Oturumunuz kapatıldı.')
    return redirect('index')
