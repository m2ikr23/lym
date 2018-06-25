from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy 
from django.views.generic import View, DetailView,ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CreateForm,ImageUploadForm,UpdateUserForm,DesactivateUserForm

from .models import User
from cirujano.models import Cirujano,Cita
from paciente.models import Paciente

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
    success_url = reverse_lazy('users:notificacion')
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
        if(request.user.is_medical):
            citas = Cita.objects.filter(medico = Cirujano.objects.get(pk=request.user.pk))
            return render(request, 'cirujano/dash_cirujano.html',{'citas':citas,'user':request.user})
        if(request.user.is_pacient):
            try:
                cita = Cita.objects.get(paciente = Paciente.objects.get(pk= request.user.pk))
            except:
                cita = None
           
            return render(request, 'paciente/dash_paciente.html',{'cita':cita})
        if(request.user.is_staff):
            return render(request, 'admin/dash_admin.html',{})


class CirujanosView(ListView):
    model = Cirujano
    template_name = "admin/dash_cirujanos.html"
    context_object_name = "cirujanos"


def clinicaDashView(request):
    return render(request,'admin/dash_clinica.html')

def quirofanoDashView(request):
    return render(request,'admin/dash_quirofano.html')

def cirugiaDashView(request):
    return render(request,'admin/dash_cirugias.html')

def especialidadDashView(request):
    return render(request,'admin/dash_especialidad.html')

def paqueteDashView(request):
    return render(request,'admin/dash_paquetes.html')


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
   

class CirujanoDeleteView(DeleteView):
    model = Cirujano
    template_name = "users/object_delete_confirm.html"
    success_url = reverse_lazy('users:cirujanos')
    
def notificacionView(request):
 return render(request,'users/notificacion.html')

def notificacionCitaView(request):
 return render(request,'users/notificacion_cita.html')

def notificacionPaqueteView(request):
 return render(request,'users/notificacion_paquete.html')

def notificacionFailView(request):
 return render(request,'users/notificacion_fail.html')

def notificacionFailPaqueteView(request):
 return render(request,'users/notificacion_fail_paquete.html')

def notificacionFailHistoriaView(request):
 return render(request,'users/notificacion_fail_historia.html')

def notificacionFailPlanificarView(request):
 return render(request,'users/notificacion_fail_Planificar.html')



class DesactivateView(UpdateView):

    model = User
    template_name ='users/desactivate.html'
    success_url = reverse_lazy('users:cirujanos')
    form_class = DesactivateUserForm 

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ActivateView(UpdateView):

    model = User
    template_name ='users/activate.html'
    success_url = reverse_lazy('users:cirujanos')
    form_class = DesactivateUserForm 
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())