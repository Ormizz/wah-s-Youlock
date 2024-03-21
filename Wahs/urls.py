"""
URL configuration for ProjetWah project.

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.connexion, name='connexion'),
    path('cv/', views.cv, name='cv'),
    path('appel_offres/', views.appel_offres, name='appel_offres'),
    path('ajouter_offres/', views.ajouter_offres, name='ajouter_offres'),
    path('postuler/', views.postuler, name='postuler'),
    path('ajouter_personnel/', views.ajouter_personnel, name='ajouter_personnel'),
    path('ajouter_utilisateur/', views.ajouter_utilisateur, name='ajouter_utilisateur'),
    path('pays/', views.pays, name='pays'),
    path('entreprise/', views.entreprise, name='entreprise'),
    path('experiences/', views.experiences, name='experiences'),
    path('genre/', views.genre, name='genre'),
    path('diplome/', views.diplome, name='diplome'),
    path('cursus/', views.cursus, name='cursus'),
    path('Type_contrat/', views.Type_contrat, name='Type_contrat'),
    path('specialite/', views.specialite, name='specialite'),
    path('profession/', views.profession, name='profession'),
    path('ajouter_employe/', views.ajouter_employe, name='ajouter_employe'),
    path('poste/', views.poste, name='poste'),
    path('client/', views.client, name='client'),
    path('compte_comptable/', views.compte_comptable, name='compte_comptable'),
    path('avoir_specialité/', views.avoir_specialite, name='avoir_specialite'),
    path('sit_matri/', views.sit_matri, name='sit_matri'),
    path('index/', views.index, name='index'),
    path('liste_employe/', views.liste_employe, name='liste_employe'),
    path('type_question/', views.type_question, name='type_question'),
    path('abonnement/', views.abonnement, name='abonnement'),
    path('avoir_sit_matri/', views.avoir_sit_matri, name='avoir_sit_matri'),
    path('avoir_specialite/', views.avoir_specialite, name='avoir_specialite'),
    path('avoir/', views.avoir, name='avoir'),
    path('con_traitement/',views.con_traitement, name='con_traitement'),
    path('faire_entretient/', views.faire_entretient, name='faire_entretient'),
    path('grp_utilisateur/', views.grp_utilisateur, name='grp_utilisateur'),
    path('obt_diplome/', views.obt_diplome, name='obt_diplome'),
    path('type_utilisateur/', views.grp_utilisateur, name='type_utilisateur'),

    path('backend/', include('backend.urls')),
]

