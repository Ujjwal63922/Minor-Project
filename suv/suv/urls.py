"""
URL configuration for suv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from suv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('flat/',views.flat),
    path('bs/bs/',views.bs),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/prop/',views.prop),
    path('bs/bs/buy/prop/prop/',views.prop),
    path('bs/bs/buy/prop/prop/prop/',views.prop),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/',views.buy),
    path('bs/bs/buy/service/',views.service),
    path('bs/bs/buy/service/flat/',views.flat),
    path('bs/bs/buy/service/flat/prop/',views.prop),
    path('bs/bs/buy/service/flat/prop/prop/',views.prop),
    path('bs/bs/buy/service/fh/',views.fh),
    path('bs/bs/buy/service/fh/prop/',views.prop),
    path('bs/bs/buy/service/fh/prop/prop/',views.prop),
    path('bs/bs/buy/service/plot/',views.plot),
    path('bs/bs/buy/service/plot/prop/',views.prop),
    path('bs/bs/buy/service/plot/prop/prop/',views.prop),
    path('bs/',views.bs),
    path('bs/buy/',views.buy),
    path('bs/buy/service/',views.service),
    path('bs/buy/service/flat/',views.flat),
    path('bs/buy/service/flat/prop/',views.prop),
    path('bs/buy/service/flat/prop/prop/',views.prop),
    path('bs/buy/service/fh/',views.fh),
    path('bs/buy/service/fh/prop/',views.prop),
    path('bs/buy/service/fh/prop/prop/',views.prop),
    path('bs/buy/service/plot/',views.plot),
    path('bs/buy/service/plot/prop/',views.prop),
    path('bs/buy/service/plot/prop/prop/',views.prop),
    path('bs/buy/prop/',views.prop),
    path('bs/buy/prop/prop/',views.prop),
    path('bs/buy/prop/prop/prop/',views.prop),
    path('bs/buy/prop/prop/prop/prop/',views.prop),
    path('plot/',views.plot),
    path('plot/prop/', views.prop),
    path('plot/prop/prop/', views.prop),
    path('plot/prop/prop/prop/', views.prop),
    path('plot/prop/prop/prop/prop/', views.prop),
    path('fh/', views.fh),
    path('fh/prop/', views.prop),
    path('fh/prop/prop/', views.home),
    path('fh/prop/prop/prop/', views.prop),
    path('fh/prop/prop/prop/prop/', views.prop),
    path('prop/',views.prop),
    path('prop/prop/',views.prop),
    path('prop/prop/prop/',views.prop),
    path('prop/prop/prop/prop/',views.prop),
    path('prop/prop/prop/prop/prop/',views.prop),
]