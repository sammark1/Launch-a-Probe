from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing.as_view(), name="Landing"),
    path('launch/', views.Launch.as_view(), name="Launch"),
    path('systems/', views.Systems_List.as_view(), name="Systems_List"),

]