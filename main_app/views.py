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

class Landing(TemplateView):
    template_name = "landing.html"

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
    fields = ['designation','name','system_type']
    template_name = "system_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.discoverer = self.request.user

        self.object.designation = designation(self.request.user.username)

        self.object.save()
        return HttpResponseRedirect('/systems')

# ==========USER/AUTH=========

def profile(request, username):
    user = User.objects.get(username=username)
    systems = System.objects.filter(discoverer=user)
    return render(request, 'profile.html', {'username': username, 'systems': systems})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('logging in ', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return render(request, 'login.html', {'form': form})
            else:
                print('The username and/or password is incorrect.')
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})
            # raise ValidationError('this is an error')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

