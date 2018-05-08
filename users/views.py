from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,CreateForm

def loginView(request):
   
    message = None
    if request.method =='POST':
        email_post = request.POST['email']
        password_post =  request.POST['password']
        user = authenticate(username=email_post, password=password_post)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect('users:dashboard')
        else:
            message = 'email o password incorrecto '

    form = LoginForm()
    context = {
        'form' : form,
        'message' : message
           }
    return render(request,'users/login.html',context)

def logoutView(request):
    logout(request)
    return redirect('users:home')


def createView(request):
    formC = CreateForm()
    context = {
        'formC':formC
    }
    return render(request,'users/create.html',context)


def homeView(request):
    return render(request,'home/home.html')

@login_required(login_url = 'users : login')
def dashboardView(request):
    return render(request, 'users/dashboard.html')
