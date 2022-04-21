from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import System
from django.core.exceptions import ValidationError
from .static.scripts.generator import *

# Views

# class Landing(TemplateView):
#     template_name = "landing.html"

class Launch(TemplateView):
    template_name = "launch.html"

# ===========SYSTEMS==========

class Systems_List(TemplateView):
    template_name = "systems_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["systems"] = System.objects.all()
        return context

class System_View(DetailView):
    model = System
    template_name = "system_view.html"

class System_Create(CreateView):
    model = System
    fields = ['system_type']
    template_name = "system_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)

        user = self.request.user

        self.object.discoverer = user

        self.object.designation = gen_system_designation(user.username,System.objects.filter(discoverer=user))

        self.object.name = gen_system_name()

        self.object.save()
        return HttpResponseRedirect('/systems')

# ==========USER/AUTH=========

def profile(request, username):
    user = User.objects.get(username=username)
    systems = System.objects.filter(discoverer=user)
    return render(request, 'profile.html', {'username': username, 'systems': systems})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def landing_view(request):
    if request.method == 'POST':
        form1 = AuthenticationForm(request, request.POST)
        form2 = UserCreationForm(request.POST)
        if form1.is_valid():
            u = form1.cleaned_data['username']
            p = form1.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return render(request, 'login.html', {'form1': form1, 'form2':form2})
            else:
                print('The username and/or password is incorrect.')
                return render(request, 'login.html', {'form1': form1, 'form2':form2})
        elif form2.is_valid():
            user = form2.save()
            login(request, user)
            print('logging in ', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'login.html', {'form1': form1, 'form2':form2})
            # raise ValidationError('this is an error')
    else:
        form1 = AuthenticationForm()
        form2 = UserCreationForm()
        return render(request, 'login.html', {'form1': form1, 'form2':form2})

