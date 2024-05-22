from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as members_views

app_name = 'accounts'

urlpatterns = [
    path('register/',members_views.register, name='register'),
    #django will normaly look the login template in registration/login.html
    #we can create create it in the members App but we want to it this way
    path('login/',auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='members/logout.html'), name='logout'),
    path('profile/',members_views.profile, name='profile'),
]