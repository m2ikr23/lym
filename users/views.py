from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy 
from django.views.generic import View, DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CreateForm,ImageUploadForm,UpdateUserForm

from .models import User

class LoginView(View):

    form = LoginForm()
    message = None
    template = 'users/login.html'

    def get(self,request,*args,**kwargs):

        if request.user.is_authenticated:
            return redirect('users:dashboard')

        return render(request,self.template,self.get_context() )
    
    def post(self,request,*args,**kwargs):

        email_post = request.POST['email']
        password_post =  request.POST['password']
        user = authenticate(username=email_post, password=password_post)

        if user is not None:
                login(request,user)
                return redirect('users:dashboard')
        else:
            self.message = 'email o password incorrecto '
        return render(request,self.template,self.get_context() )

    def get_context(self):
        return {'form':self.form,'message':self.message}


def logoutView(request):
    logout(request)
    return redirect('users:login')


class CrearView(CreateView):
    success_url = reverse_lazy('users:login')
    template_name = 'users/create.html'
    model = User
    form_class = CreateForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.is_staff = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateUserView(UpdateView):

    model = User
    template_name ='users/update.html'
    success_url = reverse_lazy('users:dashboard')

    form_class = UpdateUserForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        print(self.object.avatar)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        
    def get_object(self,queryset = None):
        return self.request.user

class editFotoView(UpdateView):

    model = User
    template_name ='users/update.html'
    success_url = reverse_lazy('users:dashboard')
    form_class = ImageUploadForm 

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.avatar = form.cleaned_data['avatar']
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        
    
    def get_object(self, queryset = None):
        return self.request.user
           

def homeView(request):
    return render(request,'home/home.html')

class DashboardView(LoginRequiredMixin,View):

    login_url = 'users:login'

    def get(self,request,*args,**kwargs):
      
        return render(request, 'users/dashboard.html',{})

class ShowView(DetailView):
    model = User
    template_name = 'users/show.html'
    queryset = model.objects.all()
    
    def get_object(self):

        object = super().get_object()

        return object

    def get_context_data(self,**kwargs):

        context = super().get_context_data(**kwargs)
        context ['user_list'] = User.objects.all()

        return context
   
    