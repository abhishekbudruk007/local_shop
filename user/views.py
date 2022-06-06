from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import make_password, check_password
from .forms import RegistrationForm, ChangePassForm
from .models import CustomUsers

# Create your views here.


def login(request):
    print('this is login page')
    return render(request, 'user/login.html')

def auth_user(request):
    username_str = request.POST.get('username')
    password_str = request.POST.get('password')
    if username_str and password_str:
        try:
            user = authenticate(username = username_str, password = password_str)
        except:
            messages.error(request, 'Username/Password Incorrect')
            return HttpResponseRedirect('login')
        if user is not None:
            auth_login(request, user)
            request.session['username']=username_str
            # messages.success(request, "User is logged In")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, 'Username/Password is Incorrect')
            return HttpResponseRedirect('login')
    else:
        messages.error(request, 'Enter username or password')



def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return HttpResponseRedirect('login')



def register(request):
    registration_form = RegistrationForm()
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST, request.FILES) #post and get will take field data and image data respectively
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, "Registration is successful")
            return HttpResponseRedirect('login')
            # return HttpResponse("registered")
        else:
            # messages.error(request, "Registration unsuccessful")
            return HttpResponseRedirect('register')
    else:
        return render(request, 'user/register.html', context={"form":registration_form})

def changepass(request):

    # changepass_form = ChangePassForm(request.user, request.POST)
     # return render(request, 'user/changepass.html',)
    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        con_new_password = request.POST['confirm_new_password']
        user=CustomUsers.objects.filter(username=request.user.username)[0]
        if check_password(old_password, user.password):
            user.password = make_password(new_password)
            user.save()
            messages.success(request, "your password was changed successful")
        return HttpResponseRedirect('login')
    else:
        # messages.error(request, " password change unsuccessful")
        return render(request, 'user/changepass.html')
        # return render(request, 'user/changepass.html', context={"form1": changepass_form})



        # changepass_form = ChangePassForm(request.user, request.POST)
        #     if changepass_form.is_valid():
        #         user=changepass_form.save()
        #         changepass_form.update()
        #         messages.success(request, "ur pass was changed successful")
        #         return HttpResponseRedirect('changepass')
        #
        # else:
        #     changepass_form = ChangePassForm(request.user)
        #     return render(request, 'user/changepass.html', context={"form1":changepass_form})


# def changepass(request):
#     # changepass_form = ChangePassForm()
#      if request.method == 'POST':
#         changepass_form = ChangePassForm(request.POST)
#         if changepass_form.is_valid():
#             new_pass = changepass_form.cleaned_data['new_password']
#             # get the current user object as user
#             if request.user.username.old_password == '':
#                 # it's first time user is changing password
#                 # populate our Members old_password_field
#                 request.user.username.old_password = request.user.username.password
#             else:
#                 request.user.username.old_password = request.user.username.old_password + ',' + request.user.username.password
#             request.user.username.password = new_pass
#             request.user.username.save()