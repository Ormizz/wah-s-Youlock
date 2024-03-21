from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def base(request):

    return render(request, 'base.html')

def connexion(request):
    return render(request, 'connexion.html')

def cv(request : HttpResponse) -> HttpResponse :
    return render(request, 'cv.html')

def appel_offres(request):
    return render(request, 'appel_offres.html')

def ajouter_offres(request):
    return render(request, 'ajouter_offres.html')

def postuler(request):
    return render(request, 'postuler.html')

def ajouter_personnel(request):
    return render(request, 'ajouter_personnel.html')

def ajouter_utilisateur(request):
    return render(request, 'ajouter_utilisateur.html')

def pays(request):
    return render(request, 'pays.html')

def entreprise(request):
    return render(request, 'entreprise.html')

def experiences(request):
    return render(request, 'experiences.html')

def genre(request):
    return render(request, 'genre.html')

def diplome(request):
    return render(request, 'diplome.html')


def cursus(request):
    return render(request, 'cursus.html')

def Type_contrat(request):
    return render(request, 'Type_contrat.html')

def specialite(request):
    return render(request, 'specialite.html')

def profession(request):
    return render(request, 'profession.html')

def poste(request):
    return render(request, 'poste.html')

def client(request):
    return render(request, 'client.html')


def compte_comptable(request):
    return render(request, 'compte_comptable.html')

def avoir_specialite(request):
    return render(request, 'avoir_specialite.html')

def ajouter_employe(request):
    return render(request, 'ajouter_employe.html')

def sit_matri(request):
    return render(request, 'sit_matri.html')

def type_question(request):
    return render(request, 'type_question.html')






def abonnement(request):
    return render(request, 'abonnement.html')
    

def avoir_sit_matri(request):
    return render(request, 'avoir_sit_matri.html')

def avoir_specialite(request):
    return render(request, 'avoir_specialite.html')

def avoir(request):
    return render(request, 'avoir.html')

def con_traitement(request):
    return render(request, 'con_traitement.html')

def faire_entretient(request):
    return render(request, 'faire_entretient.html')

def grp_utilisateur(request):
    return render(request, 'grp_utilisateur.html')

def obt_diplome(request):
    return render(request, 'obt_diplome.html')

def liste_employe(request):
    return render(request, 'liste_employe.html')
def index(request):
    return render(request, 'index.html')