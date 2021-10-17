from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User
from django.core.mail import send_mail
from random import randint
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        rp = request.POST
        user = User.objects.get(email = rp['email'])
        user = authenticate(
            request, email=rp['email'], password=rp['password'])
        if user is not None:
            print('user found')
            if user.active == True:
                print('user active')
                login(request,user)
                messages.success(request, 'You logged in')
                return redirect('Main:index')
            else:
                print('user not avtive')
                messages.error(request, 'Your account is not active. first active')
                return redirect('Accounts:activation')
        else:
            print('user not found')
            messages.error(request, 'Email or password was wrong.')
            return redirect('Accounts:login')
    else:
        return render(request, 'Accounts/log.html')


def user_signup(request):
    if request.method == 'POST':
        rp = request.POST
        code = randint(10000, 99999)
        try:
            User.objects.create_user(rp['first_name'], rp['last_name'], rp['username'], rp['email'], rp['password'], code)
        except:
            User.objects.create_user(rp['username'], rp['email'], rp['password'], code)
        
        send_mail(
            'Activation code',
            f'Hello {rp["first_name"]} {rp["last_name"]}. Your code is {code}. Please enter your code in form.',
            'shoptest20001@gmail.com',
            [rp['email']],
            fail_silently=False,
        )
        messages.success(request,'You sign up. Now active')
        return redirect('Accounts:activation')
    else:
        return render(request, 'Accounts/log.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'You logged out.')
    return redirect('Main:index')

def activation(request):
    if request.method == 'POST':
        rp = request.POST
        user = User.objects.get(email = rp['email'])
        if rp['code'] == user.code:
            user.active = True
            user.save()
            messages.success(request, f'Wellcome {user.username}. Your account is active. Now login')
        else:
            messages.error(request,'This code was wrong.')
            return redirect('Accounts:activation')
        return redirect('Accounts:login')
    else:
        return render(request, 'Accounts/activation.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        user = User.objects.get(email = request.user)
        if user.check_password(request.POST['old_password']):
            if request.POST['new_password'] == '':
                messages.error(request,'Please enter new password.')
                return redirect('Accounts:change_password')
            else:
                user.set_password(request.POST['new_password'])
                user.save()
                messages.success(request, 'Your password was changed.')
                return redirect('Accounts:login')
        else:
            messages.error(request,'This old password is wrong.')
            return redirect('Accounts:change_password')
    else:
        return render(request, 'Accounts/change_password.html')



def check_email(request):
    if request.method == 'POST':
        rp = request.POST
        user = User.objects.get(email = rp['email'])
        if user is not None:
            user.code = randint(10000, 99999)
            user.save()
            send_mail(
                'Forget password',
                f'Hello {user.first_name} {user.last_name}. Your code is {user.code}. Please enter your code in form.',
                'shoptest20001@gmail.com',
                [rp['email']],
                fail_silently=False,
            )
            messages.success(request, 'Code is send')
            return redirect('Accounts:forget_password')
        else:
            messages.error(request, 'This email is wrong')
            return redirect('Accounts:check_email')
    else:
        return render(request, 'Accounts/check_email.html')



def forget_password(request):
    if request.method == 'POST':
        rp = request.POST
        user = User.objects.get(email = rp['email'])
        if user.code == rp['code']:
            user.set_password(request.POST['new_password'])
            user.save()
            messages.success(request, 'Your password was changed.')
            return redirect('Accounts:login')
        else:
            messages.error(request, 'This code is wrong')
            return redirect('Accounts:forget_password')
    else:
        return render(request, 'Accounts/forget_password.html')
