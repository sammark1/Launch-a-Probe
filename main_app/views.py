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
from .models import System, Star_Object, Planetoid
from django.core.exceptions import ValidationError
from .static.scripts.generator import *
import json



# Views

# class Landing(TemplateView):
#     template_name = "landing.html"

class Launch(TemplateView):
    template_name = "launch.html"
# =========STAR OBJECTS=======

def Star_View(request, star_id):
    star = Star_Object.objects.get(id=star_id)
    system = System.objects.get(name=star.system.name)
    discoverer = User.objects.get(username=system.discoverer)
    return render(request, 'star_view.html', {'star':star,'system':system,'discoverer':discoverer})

def Star_Create(system):
    star_instance=Star_Object.objects.create(
        designation=gen_star_designation(system),
        name="testE",
        mass=10,
        system_id=system.id,
        )
    star_instance.save()

# =====PLANETOID OBJECTS======

def Planetoid_View(request, planetoid_id):
    planetoid = Planetoid.objects.get(id=planetoid_id)
    system = System.objects.get(name=planetoid.system.name)
    discoverer = User.objects.get(username=system.discoverer)
    return render(request, 'planet_view.html', {'planetoid':planetoid,'system':system,'discoverer':discoverer})

def Planet_Create(system):
    planetoid_instance=Planetoid.objects.create(
        designation=gen_planet_designation(system),
        name="test_AB",
        mass=199,
        system_id=system.id,
        )
    planetoid_instance.save()


# ===========SYSTEMS==========

class Systems_List(TemplateView):
    template_name = "systems_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["systems"] = System.objects.all()

        render_data={
            'bodyColor':0xffffff,
        }
        f = open("main_app/static/scripts/render_data.json", "w")
        f.write(json.dumps(render_data))
        f.close()

        return context

# class System_View(DetailView):
#     model = System
#     template_name = "system_view.html"

def System_View(request, system_id):
    system = System.objects.get(id=system_id)
    stars = Star_Object.objects.filter(system=system)
    planetoids = Planetoid.objects.filter(system=system)
    return render(request, 'system_view.html', {'system':system,'stars':stars, 'planetoids':planetoids})


class System_Create(CreateView):
    model = System
    fields = []
    template_name = "system_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)

        user = self.request.user

        self.object.discoverer = user

        self.object.designation = gen_system_designation(user.username,System.objects.filter(discoverer=user))

        self.object.name = gen_system_name()
        
        self.object.system_type = gen_system_type()

        self.object.save()
        
        # ANCHOR star creation TODO make system adaptive to system stars
        Star_Create(self.object)

        # ANCHOR planet creation
        Planet_Create(self.object)
 
        return HttpResponseRedirect(f'/system/{self.object.id}')


# ==========USER/AUTH=========

def profile(request, username):
    user = User.objects.get(username=username)
    systems = System.objects.filter(discoverer=user)
    return render(request, 'profile.html', {'username': username, 'systems': systems})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def landing_view(request): #includes login and signup
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

