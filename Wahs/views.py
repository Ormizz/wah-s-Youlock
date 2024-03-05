from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def connexion(request):
    return render(request, 'connexion.html')

def cv(request):
    return render(request, 'cv.html')

def appel_offres(request):
    return render(request, 'appel_offres.html')

def ajouter_offres(request):
    return render(request, 'ajouter_offres.html')

def postuler(request):
    return render(request, 'postuler.html')

def ajouter_personnel(request):
    return render(request, 'ajouter_personnel.html')