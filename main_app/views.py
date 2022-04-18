from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Landing(TemplateView):
    template_name = "landing.html"

class Launch(TemplateView):
    template_name = "launch.html"