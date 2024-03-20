# Dans backend/urls.py
from django.urls import path
from . import views
from .views import gct03_create


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

    # GCT08
    path('gct08/', views.gct08_list, name='gct08_list'),
    path('gct08/create/', views.gct08_create, name='gct08_create'),
    path('gct08/<int:pk>/update/', views.gct08_update, name='gct08_update'),
    path('gct08/<int:pk>/delete/', views.gct08_delete, name='gct08_delete'),

# GCT14
    path('gct14/', views.gct14_list, name='gct14_list'),
    path('gct14/create/', views.gct14_create, name='gct14_create'),
    path('gct14/<int:pk>/update/', views.gct14_update, name='gct14_update'),
    path('gct14/<int:pk>/delete/', views.gct14_delete, name='gct14_delete'),

# GCT03
    path('gct03/', views.gct03_list, name='gct03_list'),
    path('gct03/create/', views.gct03_create, name='gct03_create'),
    path('gct03/<int:pk>/update/', views.gct03_update, name='gct03_update'),
    path('gct03/<int:pk>/delete/', views.gct03_delete, name='gct03_delete'),

# GCT16
    path('gct16/', views.gct16_list, name='gct16_list'),
    path('gct16/create/', views.gct16_create, name='gct16_create'),
    path('gct16/<int:pk>/update/', views.gct16_update, name='gct16_update'),
    path('gct16/<int:pk>/delete/', views.gct16_delete, name='gct16_delete'),

# GCT24
    path('gct24/', views.gct24_list, name='gct24_list'),
    path('gct24/create/', views.gct24_create, name='gct24_create'),
    path('gct24/<int:pk>/update/', views.gct24_update, name='gct24_update'),
    path('gct24/<int:pk>/delete/', views.gct24_delete, name='gct24_delete'),

# GCT42
    # path('gct42/', views.gct42_list, name='gct42_list'),
    # path('gct42/create/', views.gct42_create, name='gct42_create'),
    # path('gct42/<int:pk>/update/', views.gct42_update, name='gct42_update'),
    # path('gct42/<int:pk>/delete/', views.gct42_delete, name='gct42_delete'),

# GCT39
    # path('gct39/', views.gct39_list, name='gct39_list'),
    # path('gct39/create/', views.gct39_create, name='gct39_create'),
    # path('gct39/<int:pk>/update/', views.gct39_update, name='gct39_update'),
    # path('gct39/<int:pk>/delete/', views.gct39_delete, name='gct39_delete'),

# GCT29
    path('gct29/', views.gct29_list, name='gct29_list'),
    path('gct29/create/', views.gct29_create, name='gct29_create'),
    path('gct29/<int:pk>/update/', views.gct29_update, name='gct29_update'),
    path('gct29/<int:pk>/delete/', views.gct29_delete, name='gct29_delete'),

# GCT50
    # path('gct50/', views.gct50_list, name='gct50_list'),
    # path('gct50/create/', views.gct50_create, name='gct50_create'),
    # path('gct50/<int:pk>/update/', views.gct50_update, name='gct50_update'),
    # path('gct50/<int:pk>/delete/', views.gct50_delete, name='gct50_delete'),

# GCT54
    # path('gct54/', views.gct54_list, name='gct54_list'),
    # path('gct54/create/', views.gct54_create, name='gct54_create'),
    # path('gct54/<int:pk>/update/', views.gct54_update, name='gct54_update'),
    # path('gct54/<int:pk>/delete/', views.gct54_delete, name='gct54_delete'),

# GCT22
    path('gct22/', views.gct22_list, name='gct22_list'),
    path('gct22/create/', views.gct22_create, name='gct22_create'),
    path('gct22/<int:pk>/update/', views.gct22_update, name='gct22_update'),
    path('gct22/<int:pk>/delete/', views.gct22_delete, name='gct22_delete'),

# GCT32
    path('gct32/', views.gct32_list, name='gct32_list'),
    path('gct32/create/', views.gct32_create, name='gct32_create'),
    path('gct32/<int:pk>/update/', views.gct32_update, name='gct32_update'),
    path('gct32/<int:pk>/delete/', views.gct32_delete, name='gct32_delete'),

# GCT35
    path('gct35/', views.gct35_list, name='gct35_list'),
    path('gct35/create/', views.gct35_create, name='gct35_create'),
    path('gct35/<int:pk>/update/', views.gct35_update, name='gct35_update'),
    path('gct35/<int:pk>/delete/', views.gct35_delete, name='gct35_delete'),

# GCT34
    path('gct34/', views.gct34_list, name='gct34_list'),
    path('gct34/create/', views.gct34_create, name='gct34_create'),
    path('gct34/<int:pk>/update/', views.gct34_update, name='gct34_update'),
    path('gct34/<int:pk>/delete/', views.gct34_delete, name='gct34_delete'),

# GCT41
    # path('gct41/', views.gct41_list, name='gct41_list'),
    # path('gct41/create/', views.gct41_create, name='gct41_create'),
    # path('gct41/<int:pk>/update/', views.gct41_update, name='gct41_update'),
    # path('gct41/<int:pk>/delete/', views.gct41_delete, name='gct41_delete'),

# GCT40
    # path('gct40/', views.gct40_list, name='gct40_list'),
    # path('gct40/create/', views.gct40_create, name='gct40_create'),
    # path('gct40/<int:pk>/update/', views.gct40_update, name='gct40_update'),
    # path('gct40/<int:pk>/delete/', views.gct40_delete, name='gct40_delete'),

# GCT13
    path('gct13/', views.gct13_list, name='gct13_list'),
    path('gct13/create/', views.gct13_create, name='gct13_create'),
    path('gct13/<int:pk>/update/', views.gct13_update, name='gct13_update'),
    path('gct13/<int:pk>/delete/', views.gct13_delete, name='gct13_delete'),

# GCT38
   path('gct38/', views.gct38_list, name='gct38_list'),
   path('gct38/create/', views.gct38_create, name='gct38_create'),
    path('gct38/<int:pk>/update/', views.gct38_update, name='gct38_update'),
    path('gct38/<int:pk>/delete/', views.gct38_delete, name='gct38_delete'),

# GCT17
    path('gct17/', views.gct17_list, name='gct17_list'),
    path('gct17/create/', views.gct17_create, name='gct17_create'),
    path('gct17/<int:pk>/update/', views.gct17_update, name='gct17_update'),
    path('gct17/<int:pk>/delete/', views.gct17_delete, name='gct17_delete'),

# GCT21
    path('gct21/', views.gct21_list, name='gct21_list'),
    path('gct21/create/', views.gct21_create, name='gct21_create'),
    path('gct21/<int:pk>/update/', views.gct21_update, name='gct21_update'),
    path('gct21/<int:pk>/delete/', views.gct21_delete, name='gct21_delete'),

# GCT18
    path('gct18/', views.gct18_list, name='gct18_list'),
    path('gct18/create/', views.gct18_create, name='gct18_create'),
    path('gct18/<int:pk>/update/', views.gct18_update, name='gct18_update'),
    path('gct18/<int:pk>/delete/', views.gct18_delete, name='gct18_delete'),

# GCT07
    path('gct07/', views.gct07_list, name='gct07_list'),
    path('gct07/create/', views.gct07_create, name='gct07_create'),
    path('gct07/<int:pk>/update/', views.gct07_update, name='gct07_update'),
    path('gct07/<int:pk>/delete/', views.gct07_delete, name='gct07_delete'),

# GCT31
    path('gct31/', views.gct31_list, name='gct31_list'),
    path('gct31/create/', views.gct31_create, name='gct31_create'),
    path('gct31/<int:pk>/update/', views.gct31_update, name='gct31_update'),
    path('gct31/<int:pk>/delete/', views.gct31_delete, name='gct31_delete'),

# GCT11
    path('gct11/', views.gct11_list, name='gct11_list'),
    path('gct11/create/', views.gct11_create, name='gct11_create'),
    path('gct11/<int:pk>/update/', views.gct11_update, name='gct11_update'),
    path('gct11/<int:pk>/delete/', views.gct11_delete, name='gct11_delete'),

# GCT55
    # path('gct55/', views.gct55_list, name='gct55_list'),
    # path('gct55/create/', views.gct55_create, name='gct55_create'),
    # path('gct55/<int:pk>/update/', views.gct55_update, name='gct55_update'),
    # path('gct55/<int:pk>/delete/', views.gct55_delete, name='gct55_delete'),

# GCT46
    # path('gct46/', views.gct46_list, name='gct46_list'),
    # path('gct46/create/', views.gct46_create, name='gct46_create'),
    # path('gct46/<int:pk>/update/', views.gct46_update, name='gct46_update'),
    # path('gct46/<int:pk>/delete/', views.gct46_delete, name='gct46_delete'),

# GCT45
    # path('gct45/', views.gct45_list, name='gct45_list'),
    # path('gct45/create/', views.gct45_create, name='gct45_create'),
    # path('gct45/<int:pk>/update/', views.gct45_update, name='gct45_update'),
    # path('gct45/<int:pk>/delete/', views.gct45_delete, name='gct45_delete'),

#GCT37
    path('gct37/', views.gct37_list, name='gct37_list'),
   path('gct37/create/', views.gct37_create, name='gct37_create'),
   path('gct37/<int:pk>/update/', views.gct37_update, name='gct37_update'),
  path('gct37/<int:pk>/delete/', views.gct37_delete, name='gct37_delete'),

# GCT52
    # path('gct52/', views.gct52_list, name='gct52_list'),
    # path('gct52/create/', views.gct52_create, name='gct52_create'),
    # path('gct52/<int:pk>/update/', views.gct52_update, name='gct52_update'),
    # path('gct52/<int:pk>/delete/', views.gct52_delete, name='gct52_delete'),

# GCT51
    # path('gct51/', views.gct51_list, name='gct51_list'),
    # path('gct51/create/', views.gct51_create, name='gct51_create'),
    # path('gct51/<int:pk>/update/', views.gct51_update, name='gct51_update'),
    # path('gct51/<int:pk>/delete/', views.gct51_delete, name='gct51_delete'),

# GCT43
    # path('gct43/', views.gct43_list, name='gct43_list'),
    # path('gct43/create/', views.gct43_create, name='gct43_create'),
    # path('gct43/<int:pk>/update/', views.gct43_update, name='gct43_update'),
    # path('gct43/<int:pk>/delete/', views.gct43_delete, name='gct43_delete'),

# GCT09
    path('gct09/', views.gct09_list, name='gct09_list'),
    path('gct09/create/', views.gct09_create, name='gct09_create'),
    path('gct09/<int:pk>/update/', views.gct09_update, name='gct09_update'),
    path('gct09/<int:pk>/delete/', views.gct09_delete, name='gct09_delete'),

# GCT02
    path('gct02/', views.gct02_list, name='gct02_list'),
    path('gct02/create/', views.gct02_create, name='gct02_create'),
    path('gct02/<int:pk>/update/', views.gct02_update, name='gct02_update'),
    path('gct02/<int:pk>/delete/', views.gct02_delete, name='gct02_delete'),

# GCT04
    path('gct04/', views.gct04_list, name='gct04_list'),
    path('gct04/create/', views.gct04_create, name='gct04_create'),
    path('gct04/<int:pk>/update/', views.gct04_update, name='gct04_update'),
    path('gct04/<int:pk>/delete/', views.gct04_delete, name='gct04_delete'),

# GCT05
    path('gct05/', views.gct05_list, name='gct05_list'),
    path('gct05/create/', views.gct05_create, name='gct05_create'),
    path('gct05/<int:pk>/update/', views.gct05_update, name='gct05_update'),
    path('gct05/<int:pk>/delete/', views.gct05_delete, name='gct05_delete'),

# GCT10
    path('gct10/', views.gct10_list, name='gct10_list'),
    path('gct10/create/', views.gct10_create, name='gct10_create'),
    path('gct10/<int:pk>/update/', views.gct10_update, name='gct10_update'),
    path('gct10/<int:pk>/delete/', views.gct10_delete, name='gct10_delete'),

# GCT15
    path('gct15/', views.gct15_list, name='gct15_list'),
    path('gct15/create/', views.gct15_create, name='gct15_create'),
    path('gct15/<int:pk>/update/', views.gct15_update, name='gct15_update'),
    path('gct15/<int:pk>/delete/', views.gct15_delete, name='gct15_delete'),

# GCT25
    path('gct25/', views.gct25_list, name='gct25_list'),
    path('gct25/create/', views.gct25_create, name='gct25_create'),
    path('gct25/<int:pk>/update/', views.gct25_update, name='gct25_update'),
    path('gct25/<int:pk>/delete/', views.gct25_delete, name='gct25_delete'),

# GCT19
    path('gct19/', views.gct19_list, name='gct19_list'),
    path('gct19/create/', views.gct19_create, name='gct19_create'),
    path('gct19/<int:pk>/update/', views.gct19_update, name='gct19_update'),
    path('gct19/<int:pk>/delete/', views.gct19_delete, name='gct19_delete'),

# GCT26
    path('gct26/', views.gct26_list, name='gct26_list'),
    path('gct26/create/', views.gct26_create, name='gct26_create'),
    path('gct26/<int:pk>/update/', views.gct26_update, name='gct26_update'),
    path('gct26/<int:pk>/delete/', views.gct26_delete, name='gct26_delete'),

# GCT12
    path('gct12/', views.gct12_list, name='gct12_list'),
    path('gct12/create/', views.gct12_create, name='gct12_create'),
    path('gct12/<int:pk>/update/', views.gct12_update, name='gct12_update'),
    path('gct12/<int:pk>/delete/', views.gct12_delete, name='gct12_delete'),

# GCT30
    path('gct30/', views.gct30_list, name='gct30_list'),
    path('gct30/create/', views.gct30_create, name='gct30_create'),
    path('gct30/<int:pk>/update/', views.gct30_update, name='gct30_update'),
    path('gct30/<int:pk>/delete/', views.gct30_delete, name='gct30_delete'),

# GCT33
    path('gct33/', views.gct33_list, name='gct33_list'),
    path('gct33/create/', views.gct33_create, name='gct33_create'),
    path('gct33/<int:pk>/update/', views.gct33_update, name='gct33_update'),
    path('gct33/<int:pk>/delete/', views.gct33_delete, name='gct33_delete'),

# Question
    # path('question/', views.question_list, name='question_list'),
    # path('question/create/', views.question_create, name='question_create'),
    # path('question/<int:pk>/update/', views.question_update, name='question_update'),
    # path('question/<int:pk>/delete/', views.question_delete, name='question_delete'),

# Choice
    # path('choice/', views.choice_list, name='choice_list'),
    # path('choice/create/', views.choice_create, name='choice_create'),
    # path('choice/<int:pk>/update/', views.choice_update, name='choice_update'),
    # path('choice/<int:pk>/delete/', views.choice_delete, name='choice_delete'),

]
