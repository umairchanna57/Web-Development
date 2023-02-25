
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('' ,views.Signup, name="Signup"),
    path('Login/', views.Login, name="Login"),
    path('Home/' , views.Home, name="Home"),
    path('logout/' , views.Logout, name="logout"),
    path('Doctor/' , views.Doctor , name='Doctor'), 
    path('Appoinment', views.Appoinment , name='Appoinment'),
    path('Save' , views.Save , name='Save'), 
    path('About', views.About, name='About'),
   
       
]
