# Dans backend/urls.py
from django.urls import path
from .views import (gct44_list, gct44_create, gct44_update, gct44_delete)
from .views import (gct01_list, gct01_create, gct01_update, gct01_delete)

urlpatterns = [
    # GCT44
    path('gct44/', gct44_list, name='gct44_list'),
    path('gct44/create/', gct44_create, name='gct44_create'),
    path('gct44/<int:pk>/update/', gct44_update, name='gct44_update'),
    path('gct44/<int:pk>/delete/', gct44_delete, name='gct44_delete'),
    # Ajoutez d'autres URL en fonction de vos besoins

    # GCT01
    path('gct01/', gct01_list, name='gct01_list'),
    path('gct01/create/', gct01_create, name='gct01_create'),
    path('gct01/<int:pk>/update/', gct01_update, name='gct01_update'),
    path('gct01/<int:pk>/delete/', gct01_delete, name='gct01_delete'),
]
