# Dans backend/urls.py
from django.urls import path
from . import views


urlpatterns = [
    # GCT44
    path('gct44/', views.gct44_list, name='gct44_list'),
    path('gct44/create/', views.gct44_create, name='gct44_create'),
    path('gct44/<int:pk>/update/', views.gct44_update, name='gct44_update'),
    path('gct44/<int:pk>/delete/', views.gct44_delete, name='gct44_delete'),
    # Ajoutez d'autres URL en fonction de vos besoins

    # Quiz
    path('', views.quiz_view, name='quiz'),
    path('submit/', views.submit_view, name='submit'),

    # GCT01
    path('gct01/', views.gct01_list, name='gct01_list'),
    path('gct01/create/', views.gct01_create, name='gct01_create'),
    path('gct01/<int:pk>/update/', views.gct01_update, name='gct01_update'),
    path('gct01/<int:pk>/delete/', views.gct01_delete, name='gct01_delete'),


]
