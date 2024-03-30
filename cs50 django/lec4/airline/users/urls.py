from . import views 
from django.urls import path, include

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    
] 