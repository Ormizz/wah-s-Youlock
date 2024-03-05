"""
URL configuration for Wahs project.

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
from .views import base
from .views import cv
from .views import connexion
from .views import appel_offres
from .views import ajouter_offres
from .views import postuler
from .views import ajouter_personnel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('connexion/', connexion, name='connexion'),
    path('cv/', cv, name='cv'),
    path('appel_offres/', appel_offres, name='appel_offres'),
    path('ajouter_offres/', ajouter_offres, name='ajouter_offres'),
    path('postuler/', postuler, name='postuler'),
    path('ajouter_personnel/', ajouter_personnel, name='ajouter_personnel'),
]
