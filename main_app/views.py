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
from django.forms import ModelForm
import json
import time



# Views

class Launch(TemplateView):
    template_name = "launch.html"
# SECTION=========STAR OBJECTS=======

class Star_Update_Form(ModelForm):
    class Meta:
        model = Star_Object
        fields=['name']

def Star_View(request, star_id):
    star = Star_Object.objects.get(id=star_id)
    system = System.objects.get(name=star.system.name)
    discoverer = User.objects.get(username=system.discoverer)
    if request.method == 'POST':
        form = Star_Update_Form(request.POST)
        if form.is_valid():
            star.name = form.cleaned_data['name']
            star.save()
            return HttpResponseRedirect(f'/star/{star_id}')
        else:
            return render(request, 'star_view.html', {'system':system,'star':star, 'discoverer':discoverer, 'form':form})
    else:
        form = Star_Update_Form() #may need args
        return render(request, 'star_view.html', {'system':system,'star':star, 'discoverer':discoverer, 'form':form})

# TODO generate 
def Star_Create(system, star_index):
    star_details = gen_star_details(system)
    star_instance = Star_Object.objects.create(
        designation = gen_star_designation(system, star_index),
        name = gen_star_name(system, star_index),
        stellar_class = star_details[0], 
        mass = star_details[1],
        system_id = system.id,
        )
    star_instance.save()
# !SECTION
#SECTION=====PLANETOID OBJECTS======

class Planet_Update_Form(ModelForm):
    class Meta:
        model = Planetoid
        fields=['name']

def Planetoid_View(request, planetoid_id):
    planetoid = Planetoid.objects.get(id=planetoid_id)
    system = System.objects.get(name=planetoid.system.name)
    discoverer = User.objects.get(username=system.discoverer)
    if request.method == 'POST':
        form = Planet_Update_Form(request.POST)
        if form.is_valid():
            planetoid.name = form.cleaned_data['name']
            planetoid.save()
            return HttpResponseRedirect(f'/planet/{planetoid_id}')
        else:
            return render(request, 'planet_view.html', {'system':system,'planetoid':planetoid, 'discoverer':discoverer, 'form':form})
    else:
        form = Planet_Update_Form() #may need args
        return render(request, 'planet_view.html', {'system':system,'planetoid':planetoid, 'discoverer':discoverer, 'form':form})

# TODO planet generation details
def Planet_Create(system, planet_index):
    planetoid_instance=Planetoid.objects.create(
        designation=gen_planet_designation(system, planet_index),
        name="test_AB",
        mass=199,
        system_id=system.id,
        )
    planetoid_instance.save()

# !SECTION
#SECTION===========SYSTEMS==========

class Systems_List(TemplateView):
    template_name = "systems_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search=self.request.GET.get('search')
        if search !=None:
            context["systems"] = System.objects.filter(name__icontains=search)
        else:
            context["systems"] = System.objects.all()

        render_data={
            'bodyColor':0xffff00,
        }
        f = open("main_app/static/scripts/render_data.json", "w")
        f.write(json.dumps(render_data))
        f.close()

        return context

# class System_View(DetailView):
#     model = System
#     template_name = "system_view.html"
class System_Update_Form(ModelForm):
    class Meta:
        model = System
        fields=['name']

class System_Delete_Form(ModelForm):
    class Meta:
        model = System
        fields=[]

def System_View(request, system_id):
    system = System.objects.get(id=system_id)
    stars = Star_Object.objects.filter(system=system)
    planetoids = Planetoid.objects.filter(system=system)
    if request.method == 'POST':
        u_form = System_Update_Form(request.POST)
        d_form = System_Delete_Form(request.POST)
        if u_form.is_valid():
            system.name = u_form.cleaned_data['name']
            system.save()
            return HttpResponseRedirect(f'/system/{system_id}')
        elif d_form.is_valid():
            user = system.discoverer
            system.delete()
            return HttpResponseRedirect(f'/user/{user}')
        else:
            return render(
                request, 'system_view.html', {
                    'system':system,
                    'stars':stars, 
                    'planetoids':planetoids, 
                    'u_form':u_form, 
                    'd_form':d_form
                    })
    else:
        # ANCHOR add user as visitor to system
        # print('user: ', request.user)
        system.visitors.add(request.user)
        u_form = System_Update_Form()
        d_form = System_Delete_Form()
        return render(
            request, 'system_view.html', {
                'system':system,
                'stars':stars, 
                'planetoids':planetoids, 
                'u_form':u_form, 
                'd_form':d_form
                })

# TODO DELETEME
# def profile_update(request, username):
#     if request.method == 'POST':
#         form= Profile_Update_Form(request.POST)
#         found_user=User.objects.get(username=username)
#         recipient=Recipient.objects.get(user=found_user)
#         # print(user.username)
#         if form.is_valid():
#             # form.save()
#             biography = form.cleaned_data['bio']
#             Recipient.objects.filter(user=found_user).update(bio=biography)
#             # Recipient.objects.update(user=found_user, bio=biography)
#             return HttpResponseRedirect('/home')
#         else:
#             return render(request, 'profile_edit.html', {'form': form})
#     else:
#         user=User.objects.get(username=username)
#         recipient=Recipient.objects.get(user=user)
#         form=Profile_Update_Form(instance=recipient)
#         return render(request, 'profile_edit.html', {'form': form})

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
        
        # ANCHOR star creation
        num_stars = get_system_stars(self.object.system_type)
        for index in range(num_stars):
            Star_Create(self.object, index)

        # ANCHOR planet creation
        num_planets = get_system_planets(self.object.system_type)
        for index in range(num_planets):
            Planet_Create(self.object, index)

        # time.sleep(1)

        return HttpResponseRedirect(f'/system/scan/{self.object.id}')

def System_Scan(request, system_id):
    return render(request, 'system_scan.html',{'system_id': system_id})

# !SECTION
#SECTION==========USER/AUTH=========

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

#!SECTION