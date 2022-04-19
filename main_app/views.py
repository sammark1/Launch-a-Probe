from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import System

# Create your views here.

class Landing(TemplateView):
    template_name = "landing.html"

class Launch(TemplateView):
    template_name = "launch.html"

# class System:
#     def __init__(self, designation, name):
#         self.designation = designation
#         self.name = name

# systems = [
#     System("SA-5994", "Fitzpatrick"),
#     System("SA-5995", "Eggman"),
#     System("SA-5996", "Retired Robot"),
#     System("SA-5997", "crabpoijloe"),
# ]

class Systems_List(TemplateView):
    template_name = "systems_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["systems"] = System.objects.all()
        return context