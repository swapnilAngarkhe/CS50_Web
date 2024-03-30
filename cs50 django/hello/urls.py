from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nikhil", views.nikhil, name="nikhil"),
    path("<str:name>", views.greet, name="greet"),
    path("david", views.david, name="david")
   
    
]