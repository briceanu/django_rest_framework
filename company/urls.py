"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from drivers.views import  login, signup , get_drivers
from truck.views import create_truck, get_trucks
from working_shift.views import get_data, get_day, get_km, get_user_load, increase_km, save_working_day

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_truck',create_truck,name="create_truck"),
    path('signup',signup,name='signup'),
    path('login',login,name='login'),
    path('save_working_day',save_working_day,name='save_working_day'),
    path('get_trucks',get_trucks,name="get_trucks"),
    path('get_drivers',get_drivers,name="get_drivers"),
    path('get_day',get_day,name='get_day'),
    path('get_user_load',get_user_load, name="get_user_load"),
    path('get_data',get_data,name='get_data'),
    path('get_km',get_km,name="get_km"),
    path('increase_km',increase_km,name='increase_km')
 ]
