from django.urls import path
from . import views

urlpatterns = [
    # make sure to lowercase all url names
    path('', views.landing_view, name="Landing"),
    path('launch/', views.Launch.as_view(), name="Launch"),
    path('systems/', views.Systems_List.as_view(), name="Systems_List"),
    path('system/<int:system_id>/', views.System_View, name="System_View"),
    path('system/create/', views.System_Create.as_view(), name="System_Create"),
    path('star/<int:star_id>/', views.Star_View, name="Star_View"),
    path('planet/<int:planetoid_id>/', views.Planetoid_View, name="Planetoid_View"),
    path('user/<username>/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]