from django.urls import path
from . import views

urlpatterns = [
    # make sure to lowercase all url names
    path('', views.Landing.as_view(), name="Landing"),
    path('launch/', views.Launch.as_view(), name="Launch"),
    path('systems/', views.Systems_List.as_view(), name="Systems_List"),
    path('system/<int:pk>/', views.System_View.as_view(), name="System_View"),
    path('system/create/', views.System_Create.as_view(), name="System_Create"),
    path('user/<username>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]