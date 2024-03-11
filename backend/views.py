from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.


# CV / GCT44 
def gct44_list(request, pk):
    gct44_item = get_object_or_404(GCT44, pk=pk)
    return render(request, 'gct44_read.html', {'gct44_item': gct44_item})

def gct44_create(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        candidat_id = request.POST.get('candidat')
        profession_id = request.POST.get('profession')
        experience_id = request.POST.get('experience')
        etablissement_id = request.POST.get('etablissement')
        entreprise_id = request.POST.get('entreprise')
        loisir_id = request.POST.get('loisir')
        date = request.POST.get('date')
        # Ajouter d'autres champs selon votre modèle

        # Créer un nouvel objet GCT44
        new_gct44 = GCT44.objects.create(
            candidat=GCT07.objects.get(id=candidat_id),
            profession=GCT34.objects.get(id=profession_id),
            experience=GCT19.objects.get(id=experience_id),
            etablissement=GCT18.objects.get(id=etablissement_id),
            entreprise=GCT17.objects.get(id=entreprise_id),
            loisir=GCT24.objects.get(id=loisir_id),
            date=date
        )
        new_gct44.save()
        # Ajouter d'autres champs selon votre modèle

        return redirect('gct44_list')  # Rediriger vers la liste après ajout
    else:
        candidats = GCT07.objects.all()
        professions = GCT34.objects.all()
        experiences = GCT19.objects.all()
        etablissements = GCT18.objects.all()
        entreprises = GCT17.objects.all()
        loisirs = GCT24.objects.all()
        return render(request, 'gct44_create.html', {
            'candidats': candidats,
            'professions': professions,
            'experiences': experiences,
            'etablissements': etablissements,
            'entreprises': entreprises,
            'loisirs': loisirs,
        })  # Afficher le formulaire de création

def gct44_update(request, pk):
    gct44_item = get_object_or_404(GCT44, pk=pk)

    if request.method == 'POST':
        # Récupérer les données du formulaire
        candidat_id = request.POST.get('candidat')
        profession_id = request.POST.get('profession')
        experience_id = request.POST.get('experience')
        etablissement_id = request.POST.get('etablissement')
        entreprise_id = request.POST.get('entreprise')
        loisir_id = request.POST.get('loisir')
        date = request.POST.get('date')
        # Ajouter d'autres champs selon votre modèle

        # Mettre à jour l'objet GCT44
        gct44_item.candidat = GCT07.objects.get(id=candidat_id)
        gct44_item.profession = GCT34.objects.get(id=profession_id)
        gct44_item.experience = GCT19.objects.get(id=experience_id)
        gct44_item.etablissement = GCT18.objects.get(id=etablissement_id)
        gct44_item.entreprise = GCT17.objects.get(id=entreprise_id)
        gct44_item.loisir = GCT24.objects.get(id=loisir_id)
        gct44_item.date = date
        # Ajouter d'autres champs selon votre modèle
        gct44_item.save()

        return redirect('gct44_list')  # Rediriger vers la liste après modification
    else:
        candidats = GCT07.objects.all()
        professions = GCT34.objects.all()
        experiences = GCT19.objects.all()
        etablissements = GCT18.objects.all()
        entreprises = GCT17.objects.all()
        loisirs = GCT24.objects.all()
        return render(request, 'gct44_update.html', {
            'gct44_item': gct44_item,
            'candidats': candidats,
            'professions': professions,
            'experiences': experiences,
            'etablissements': etablissements,
            'entreprises': entreprises,
            'loisirs': loisirs,
        })

def gct44_delete(request, pk):
    gct44_item = get_object_or_404(GCT44, pk=pk)

    if request.method == 'POST':
        # Supprimer l'objet GCT44
        gct44_item.delete()
        return redirect('gct44_list')  # Rediriger vers la liste après suppression
    else:
        return render(request, 'gct44_delete.html', {'gct44_item': gct44_item})
    

# Abonnement / GCT01
# Dans views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT01

def gct01_list(request):
    gct01_items = GCT01.objects.all()
    return render(request, 'gct01_list.html', {'gct01_items': gct01_items})

def gct01_create(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        date_debut_abonnement = request.POST.get('date_debut_abonnement')
        date_fin_abonnement = request.POST.get('date_fin_abonnement')
        # Ajouter d'autres champs selon votre modèle

        # Créer un nouvel objet GCT01
        new_gct01 = GCT01.objects.create(
            date_debut_abonnement=date_debut_abonnement,
            date_fin_abonnement=date_fin_abonnement,
            # Ajouter d'autres champs selon votre modèle
        )
        new_gct01.save()
        
        return redirect('gct01_list')  # Rediriger vers la liste après ajout
    else:
        return render(request, 'gct01_create.html')  # Afficher le formulaire de création

def gct01_update(request, pk):
    gct01_item = get_object_or_404(GCT01, pk=pk)

    if request.method == 'POST':
        # Récupérer les données du formulaire
        date_debut_abonnement = request.POST.get('date_debut_abonnement')
        date_fin_abonnement = request.POST.get('date_fin_abonnement')
        # Ajouter d'autres champs selon votre modèle

        # Mettre à jour l'objet GCT01
        gct01_item.date_debut_abonnement = date_debut_abonnement
        gct01_item.date_fin_abonnement = date_fin_abonnement
        # Ajouter d'autres champs selon votre modèle
        gct01_item.save()

        return redirect('gct01_list')  # Rediriger vers la liste après modification
    else:
        return render(request, 'gct01_update.html', {'gct01_item': gct01_item})

def gct01_delete(request, pk):
    gct01_item = get_object_or_404(GCT01, pk=pk)

    if request.method == 'POST':
        # Supprimer l'objet GCT01
        gct01_item.delete()
        return redirect('gct01_list')  # Rediriger vers la liste après suppression
    else:
        return render(request, 'gct01_delete.html', {'gct01_item': gct01_item})



from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT02

def gct02_list(request):
    gct02_items = GCT02.objects.all()
    return render(request, 'gct02_list.html', {'gct02_items': gct02_items})

def gct02_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_action = request.POST.get('lib_action')
        
        # Create a new GCT02 object
        new_gct02 = GCT02.objects.create(lib_action=lib_action)
        new_gct02.save()

        return redirect('gct02_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct02_create.html')  # Display the creation form

def gct02_update(request, pk):
    gct02_item = get_object_or_404(GCT02, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_action = request.POST.get('lib_action')

        # Update the GCT02 object
        gct02_item.lib_action = lib_action
        gct02_item.save()

        return redirect('gct02_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct02_update.html', {'gct02_item': gct02_item})

def gct02_delete(request, pk):
    gct02_item = get_object_or_404(GCT02, pk=pk)

    if request.method == 'POST':
        # Delete the GCT02 object
        gct02_item.delete()
        return redirect('gct02_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct02_delete.html', {'gct02_item': gct02_item})
    
from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT03

def gct03_list(request):
    gct03_items = GCT03.objects.all()
    return render(request, 'gct03_list.html', {'gct03_items': gct03_items})

def gct03_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_appel_offre = request.POST.get('lib_appel_offre')
        client_id = request.POST.get('client')
        specialite_id = request.POST.get('specialite')
        date = request.POST.get('date')
        age_limite = request.POST.get('age_limite')
        mission_principale = request.POST.get('mission_principale')

        # Create a new GCT03 object
        new_gct03 = GCT03.objects.create(
            lib_appel_offre=lib_appel_offre,
            client_id=client_id,
            specialite_id=specialite_id,
            date=date,
            age_limite=age_limite,
            mission_principale=mission_principale
        )
        new_gct03.save()

        return redirect('gct03_list')  # Redirect to the list after creation
    else:
        clients = GCT42.objects.all()
        specialites = GCT38.objects.all()
        return render(request, 'gct03_create.html', {
            'clients': clients,
            'specialites': specialites,
        })  # Display the creation form

def gct03_update(request, pk):
    gct03_item = get_object_or_404(GCT03, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_appel_offre = request.POST.get('lib_appel_offre')
        client_id = request.POST.get('client')
        specialite_id = request.POST.get('specialite')
        date = request.POST.get('date')
        age_limite = request.POST.get('age_limite')
        mission_principale = request.POST.get('mission_principale')

        # Update the GCT03 object
        gct03_item.lib_appel_offre = lib_appel_offre
        gct03_item.client_id = client_id
        gct03_item.specialite_id = specialite_id
        gct03_item.date = date
        gct03_item.age_limite = age_limite
        gct03_item.mission_principale = mission_principale
        gct03_item.save()

        return redirect('gct03_list')  # Redirect to the list after modification
    else:
        clients = GCT42.objects.all()
        specialites = GCT38.objects.all()
        return render(request, 'gct03_update.html', {
            'gct03_item': gct03_item,
            'clients': clients,
            'specialites': specialites,
        })

def gct03_delete(request, pk):
    gct03_item = get_object_or_404(GCT03, pk=pk)

    if request.method == 'POST':
        # Delete the GCT03 object
        gct03_item.delete()
        return redirect('gct03_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct03_delete.html', {'gct03_item': gct03_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT04

def gct04_list(request):
    gct04_items = GCT04.objects.all()
    return render(request, 'gct04_list.html', {'gct04_items': gct04_items})

def gct04_create(request):
    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        situation_matrimoniale_id = request.POST.get('situation_matrimoniale')
        date = request.POST.get('date')

        # Create a new GCT04 object
        new_gct04 = GCT04.objects.create(
            candidat_id=candidat_id,
            situation_matrimoniale_id=situation_matrimoniale_id,
            date=date
        )
        new_gct04.save()

        return redirect('gct04_list')  # Redirect to the list after creation
    else:
        candidats = GCT07.objects.all()
        situations_matrimoniales = GCT37.objects.all()
        return render(request, 'gct04_create.html', {
            'candidats': candidats,
            'situations_matrimoniales': situations_matrimoniales,
        })  # Display the creation form

def gct04_update(request, pk):
    gct04_item = get_object_or_404(GCT04, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        situation_matrimoniale_id = request.POST.get('situation_matrimoniale')
        date = request.POST.get('date')

        # Update the GCT04 object
        gct04_item.candidat_id = candidat_id
        gct04_item.situation_matrimoniale_id = situation_matrimoniale_id
        gct04_item.date = date
        gct04_item.save()

        return redirect('gct04_list')  # Redirect to the list after modification
    else:
        candidats = GCT07.objects.all()
        situations_matrimoniales = GCT37.objects.all()
        return render(request, 'gct04_update.html', {
            'gct04_item': gct04_item,
            'candidats': candidats,
            'situations_matrimoniales': situations_matrimoniales,
        })

def gct04_delete(request, pk):
    gct04_item = get_object_or_404(GCT04, pk=pk)

    if request.method == 'POST':
        # Delete the GCT04 object
        gct04_item.delete()
        return redirect('gct04_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct04_delete.html', {'gct04_item': gct04_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT05

def gct05_list(request):
    gct05_items = GCT05.objects.all()
    return render(request, 'gct05_list.html', {'gct05_items': gct05_items})

def gct05_create(request):
    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        specialite_id = request.POST.get('specialite')
        date = request.POST.get('date')

        # Create a new GCT05 object
        new_gct05 = GCT05.objects.create(
            candidat_id=candidat_id,
            specialite_id=specialite_id,
            date=date
        )
        new_gct05.save()

        return redirect('gct05_list')  # Redirect to the list after creation
    else:
        candidats = GCT07.objects.all()
        specialites = GCT38.objects.all()
        return render(request, 'gct05_create.html', {
            'candidats': candidats,
            'specialites': specialites,
        })  # Display the creation form

def gct05_update(request, pk):
    gct05_item = get_object_or_404(GCT05, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        specialite_id = request.POST.get('specialite')
        date = request.POST.get('date')

        # Update the GCT05 object
        gct05_item.candidat_id = candidat_id
        gct05_item.specialite_id = specialite_id
        gct05_item.date = date
        gct05_item.save()

        return redirect('gct05_list')  # Redirect to the list after modification
    else:
        candidats = GCT07.objects.all()
        specialites = GCT38.objects.all()
        return render(request, 'gct05_update.html', {
            'gct05_item': gct05_item,
            'candidats': candidats,
            'specialites': specialites,
        })

def gct05_delete(request, pk):
    gct05_item = get_object_or_404(GCT05, pk=pk)

    if request.method == 'POST':
        # Delete the GCT05 object
        gct05_item.delete()
        return redirect('gct05_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct05_delete.html', {'gct05_item': gct05_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT06

def gct06_list(request):
    gct06_items = GCT06.objects.all()
    return render(request, 'gct06_list.html', {'gct06_items': gct06_items})

def gct06_create(request):
    if request.method == 'POST':
        # Retrieve form data
        utilisateur_id = request.POST.get('utilisateur')
        traitement_id = request.POST.get('traitement')
        date = request.POST.get('date')

        # Create a new GCT06 object
        new_gct06 = GCT06.objects.create(
            utilisateur_id=utilisateur_id,
            traitement_id=traitement_id,
            date=date
        )
        new_gct06.save()

        return redirect('gct06_list')  # Redirect to the list after creation
    else:
        utilisateurs = GCT42.objects.all()
        traitements = GCT40.objects.all()
        return render(request, 'gct06_create.html', {
            'utilisateurs': utilisateurs,
            'traitements': traitements,
        })  # Display the creation form

def gct06_update(request, pk):
    gct06_item = get_object_or_404(GCT06, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        utilisateur_id = request.POST.get('utilisateur')
        traitement_id = request.POST.get('traitement')
        date = request.POST.get('date')

        # Update the GCT06 object
        gct06_item.utilisateur_id = utilisateur_id
        gct06_item.traitement_id = traitement_id
        gct06_item.date = date
        gct06_item.save()

        return redirect('gct06_list')  # Redirect to the list after modification
    else:
        utilisateurs = GCT42.objects.all()
        traitements = GCT40.objects.all()
        return render(request, 'gct06_update.html', {
            'gct06_item': gct06_item,
            'utilisateurs': utilisateurs,
            'traitements': traitements,
        })

def gct06_delete(request, pk):
    gct06_item = get_object_or_404(GCT06, pk=pk)

    if request.method == 'POST':
        # Delete the GCT06 object
        gct06_item.delete()
        return redirect('gct06_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct06_delete.html', {'gct06_item': gct06_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT07

def gct07_list(request):
    gct07_items = GCT07.objects.all()
    return render(request, 'gct07_list.html', {'gct07_items': gct07_items})

def gct07_create(request):
    if request.method == 'POST':
        # Retrieve form data
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_naissance = request.POST.get('date_naissance')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')

        # Create a new GCT07 object
        new_gct07 = GCT07.objects.create(
            nom=nom,
            prenom=prenom,
            date_naissance=date_naissance,
            email=email,
            adresse=adresse,
            telephone=telephone
        )
        new_gct07.save()

        return redirect('gct07_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct07_create.html')  # Display the creation form

def gct07_update(request, pk):
    gct07_item = get_object_or_404(GCT07, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_naissance = request.POST.get('date_naissance')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')

        # Update the GCT07 object
        gct07_item.nom = nom
        gct07_item.prenom = prenom
        gct07_item.date_naissance = date_naissance
        gct07_item.email = email
        gct07_item.adresse = adresse
        gct07_item.telephone = telephone
        gct07_item.save()

        return redirect('gct07_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct07_update.html', {'gct07_item': gct07_item})

def gct07_delete(request, pk):
    gct07_item = get_object_or_404(GCT07, pk=pk)

    if request.method == 'POST':
        # Delete the GCT07 object
        gct07_item.delete()
        return redirect('gct07_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct07_delete.html', {'gct07_item': gct07_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT08

def gct08_list(request):
    gct08_items = GCT08.objects.all()
    return render(request, 'gct08_list.html', {'gct08_items': gct08_items})

def gct08_create(request):
    if request.method == 'POST':
        # Retrieve form data
        denomination_sociale = request.POST.get('denomination_sociale')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        # Create a new GCT08 object
        new_gct08 = GCT08.objects.create(
            denomination_sociale=denomination_sociale,
            adresse=adresse,
            telephone=telephone,
            email=email
        )
        new_gct08.save()

        return redirect('gct08_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct08_create.html')  # Display the creation form

def gct08_update(request, pk):
    gct08_item = get_object_or_404(GCT08, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        denomination_sociale = request.POST.get('denomination_sociale')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        # Update the GCT08 object
        gct08_item.denomination_sociale = denomination_sociale
        gct08_item.adresse = adresse
        gct08_item.telephone = telephone
        gct08_item.email = email
        gct08_item.save()

        return redirect('gct08_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct08_update.html', {'gct08_item': gct08_item})

def gct08_delete(request, pk):
    gct08_item = get_object_or_404(GCT08, pk=pk)

    if request.method == 'POST':
        # Delete the GCT08 object
        gct08_item.delete()
        return redirect('gct08_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct08_delete.html', {'gct08_item': gct08_item})

from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT09

def gct09_list(request):
    gct09_items = GCT09.objects.all()
    return render(request, 'gct09_list.html', {'gct09_items': gct09_items})

def gct09_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_compte_comptable = request.POST.get('lib_compte_comptable')

        # Create a new GCT09 object
        new_gct09 = GCT09.objects.create(
            lib_compte_comptable=lib_compte_comptable
        )
        new_gct09.save()

        return redirect('gct09_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct09_create.html')  # Display the creation form

def gct09_update(request, pk):
    gct09_item = get_object_or_404(GCT09, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_compte_comptable = request.POST.get('lib_compte_comptable')

        # Update the GCT09 object
        gct09_item.lib_compte_comptable = lib_compte_comptable
        gct09_item.save()

        return redirect('gct09_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct09_update.html', {'gct09_item': gct09_item})

def gct09_delete(request, pk):
    gct09_item = get_object_or_404(GCT09, pk=pk)

    if request.method == 'POST':
        # Delete the GCT09 object
        gct09_item.delete()
        return redirect('gct09_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct09_delete.html', {'gct09_item': gct09_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT10

def gct10_list(request):
    gct10_items = GCT10.objects.all()
    return render(request, 'gct10_list.html', {'gct10_items': gct10_items})

def gct10_create(request):
    if request.method == 'POST':
        # Retrieve form data
        utilisateur_id = request.POST.get('utilisateur')
        traitement_id = request.POST.get('traitement')
        date = request.POST.get('date')

        # Create a new GCT10 object
        new_gct10 = GCT10.objects.create(
            utilisateur_id=utilisateur_id,
            traitement_id=traitement_id,
            date=date
        )
        new_gct10.save()

        return redirect('gct10_list')  # Redirect to the list after creation
    else:
        utilisateurs = GCT42.objects.all()
        traitements = GCT40.objects.all()
        return render(request, 'gct10_create.html', {
            'utilisateurs': utilisateurs,
            'traitements': traitements,
        })  # Display the creation form

def gct10_update(request, pk):
    gct10_item = get_object_or_404(GCT10, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        utilisateur_id = request.POST.get('utilisateur')
        traitement_id = request.POST.get('traitement')
        date = request.POST.get('date')

        # Update the GCT10 object
        gct10_item.utilisateur_id = utilisateur_id
        gct10_item.traitement_id = traitement_id
        gct10_item.date = date
        gct10_item.save()

        return redirect('gct10_list')  # Redirect to the list after modification
    else:
        utilisateurs = GCT42.objects.all()
        traitements = GCT40.objects.all()
        return render(request, 'gct10_update.html', {
            'gct10_item': gct10_item,
            'utilisateurs': utilisateurs,
            'traitements': traitements,
        })

def gct10_delete(request, pk):
    gct10_item = get_object_or_404(GCT10, pk=pk)

    if request.method == 'POST':
        # Delete the GCT10 object
        gct10_item.delete()
        return redirect('gct10_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct10_delete.html', {'gct10_item': gct10_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT11

def gct11_list(request):
    gct11_items = GCT11.objects.all()
    return render(request, 'gct11_list.html', {'gct11_items': gct11_items})

def gct11_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_diplome = request.POST.get('lib_diplome')

        # Create a new GCT11 object
        new_gct11 = GCT11.objects.create(
            lib_diplome=lib_diplome
        )
        new_gct11.save()

        return redirect('gct11_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct11_create.html')  # Display the creation form

def gct11_update(request, pk):
    gct11_item = get_object_or_404(GCT11, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_diplome = request.POST.get('lib_diplome')

        # Update the GCT11 object
        gct11_item.lib_diplome = lib_diplome
        gct11_item.save()

        return redirect('gct11_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct11_update.html', {'gct11_item': gct11_item})

def gct11_delete(request, pk):
    gct11_item = get_object_or_404(GCT11, pk=pk)

    if request.method == 'POST':
        # Delete the GCT11 object
        gct11_item.delete()
        return redirect('gct11_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct11_delete.html', {'gct11_item': gct11_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT12

def gct12_list(request):
    gct12_items = GCT12.objects.all()
    return render(request, 'gct12_list.html', {'gct12_items': gct12_items})

def gct12_create(request):
    if request.method == 'POST':
        # Retrieve form data
        diplome_id = request.POST.get('diplome')
        etablissement_id = request.POST.get('etablissement')
        date = request.POST.get('date')

        # Create a new GCT12 object
        new_gct12 = GCT12.objects.create(
            diplome_id=diplome_id,
            etablissement_id=etablissement_id,
            date=date
        )
        new_gct12.save()

        return redirect('gct12_list')  # Redirect to the list after creation
    else:
        diplomes = GCT13.objects.all()
        etablissements = GCT18.objects.all()
        return render(request, 'gct12_create.html', {
            'diplomes': diplomes,
            'etablissements': etablissements,
        })  # Display the creation form

def gct12_update(request, pk):
    gct12_item = get_object_or_404(GCT12, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        diplome_id = request.POST.get('diplome')
        etablissement_id = request.POST.get('etablissement')
        date = request.POST.get('date')

        # Update the GCT12 object
        gct12_item.diplome_id = diplome_id
        gct12_item.etablissement_id = etablissement_id
        gct12_item.date = date
        gct12_item.save()

        return redirect('gct12_list')  # Redirect to the list after modification
    else:
        diplomes = GCT13.objects.all()
        etablissements = GCT18.objects.all()
        return render(request, 'gct12_update.html', {
            'gct12_item': gct12_item,
            'diplomes': diplomes,
            'etablissements': etablissements,
        })

def gct12_delete(request, pk):
    gct12_item = get_object_or_404(GCT12, pk=pk)

    if request.method == 'POST':
        # Delete the GCT12 object
        gct12_item.delete()
        return redirect('gct12_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct12_delete.html', {'gct12_item': gct12_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT13

def gct13_list(request):
    gct13_items = GCT13.objects.all()
    return render(request, 'gct13_list.html', {'gct13_items': gct13_items})

def gct13_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_diplome = request.POST.get('lib_diplome')

        # Create a new GCT13 object
        new_gct13 = GCT13.objects.create(
            lib_diplome=lib_diplome
        )
        new_gct13.save()

        return redirect('gct13_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct13_create.html')  # Display the creation form

def gct13_update(request, pk):
    gct13_item = get_object_or_404(GCT13, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_diplome = request.POST.get('lib_diplome')

        # Update the GCT13 object
        gct13_item.lib_diplome = lib_diplome
        gct13_item.save()

        return redirect('gct13_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct13_update.html', {'gct13_item': gct13_item})

def gct13_delete(request, pk):
    gct13_item = get_object_or_404(GCT13, pk=pk)

    if request.method == 'POST':
        # Delete the GCT13 object
        gct13_item.delete()
        return redirect('gct13_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct13_delete.html', {'gct13_item': gct13_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT14

def gct14_list(request):
    gct14_items = GCT14.objects.all()
    return render(request, 'gct14_list.html', {'gct14_items': gct14_items})

def gct14_create(request):
    if request.method == 'POST':
        # Retrieve form data
        date = request.POST.get('date')

        # Create a new GCT14 object
        new_gct14 = GCT14.objects.create(
            date=date
        )
        new_gct14.save()

        return redirect('gct14_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct14_create.html')  # Display the creation form

def gct14_update(request, pk):
    gct14_item = get_object_or_404(GCT14, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        date = request.POST.get('date')

        # Update the GCT14 object
        gct14_item.date = date
        gct14_item.save()

        return redirect('gct14_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct14_update.html', {'gct14_item': gct14_item})

def gct14_delete(request, pk):
    gct14_item = get_object_or_404(GCT14, pk=pk)

    if request.method == 'POST':
        # Delete the GCT14 object
        gct14_item.delete()
        return redirect('gct14_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct14_delete.html', {'gct14_item': gct14_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT15

def gct15_list(request):
    gct15_items = GCT15.objects.all()
    return render(request, 'gct15_list.html', {'gct15_items': gct15_items})

def gct15_create(request):
    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        test_id = request.POST.get('test')
        date = request.POST.get('date')

        # Create a new GCT15 object
        new_gct15 = GCT15.objects.create(
            candidat_id=candidat_id,
            test_id=test_id,
            date=date
        )
        new_gct15.save()

        return redirect('gct15_list')  # Redirect to the list after creation
    else:
        candidats = GCT07.objects.all()
        tests = GCT39.objects.all()
        return render(request, 'gct15_create.html', {
            'candidats': candidats,
            'tests': tests,
        })  # Display the creation form

def gct15_update(request, pk):
    gct15_item = get_object_or_404(GCT15, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        test_id = request.POST.get('test')
        date = request.POST.get('date')

        # Update the GCT15 object
        gct15_item.candidat_id = candidat_id
        gct15_item.test_id = test_id
        gct15_item.date = date
        gct15_item.save()

        return redirect('gct15_list')  # Redirect to the list after modification
    else:
        candidats = GCT07.objects.all()
        tests = GCT39.objects.all()
        return render(request, 'gct15_update.html', {
            'gct15_item': gct15_item,
            'candidats': candidats,
            'tests': tests,
        })

def gct15_delete(request, pk):
    gct15_item = get_object_or_404(GCT15, pk=pk)

    if request.method == 'POST':
        # Delete the GCT15 object
        gct15_item.delete()
        return redirect('gct15_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct15_delete.html', {'gct15_item': gct15_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT16

def gct16_list(request):
    gct16_items = GCT16.objects.all()
    return render(request, 'gct16_list.html', {'gct16_items': gct16_items})

def gct16_create(request):
    if request.method == 'POST':
        # Retrieve form data
        nom_employe = request.POST.get('nom_employe')
        prenom_employe = request.POST.get('prenom_employe')
        date_naissance = request.POST.get('date_naissance')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        # Create a new GCT16 object
        new_gct16 = GCT16.objects.create(
            nom_employe=nom_employe,
            prenom_employe=prenom_employe,
            date_naissance=date_naissance,
            adresse=adresse,
            telephone=telephone,
            email=email
        )
        new_gct16.save()

        return redirect('gct16_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct16_create.html')  # Display the creation form

def gct16_update(request, pk):
    gct16_item = get_object_or_404(GCT16, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        nom_employe = request.POST.get('nom_employe')
        prenom_employe = request.POST.get('prenom_employe')
        date_naissance = request.POST.get('date_naissance')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        # Update the GCT16 object
        gct16_item.nom_employe = nom_employe
        gct16_item.prenom_employe = prenom_employe
        gct16_item.date_naissance = date_naissance
        gct16_item.adresse = adresse
        gct16_item.telephone = telephone
        gct16_item.email = email
        gct16_item.save()

        return redirect('gct16_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct16_update.html', {'gct16_item': gct16_item})

def gct16_delete(request, pk):
    gct16_item = get_object_or_404(GCT16, pk=pk)

    if request.method == 'POST':
        # Delete the GCT16 object
        gct16_item.delete()
        return redirect('gct16_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct16_delete.html', {'gct16_item': gct16_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT17

def gct17_list(request):
    gct17_items = GCT17.objects.all()
    return render(request, 'gct17_list.html', {'gct17_items': gct17_items})

def gct17_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_entreprise = request.POST.get('lib_entreprise')
        siege_sociale = request.POST.get('siege_sociale')

        # Create a new GCT17 object
        new_gct17 = GCT17.objects.create(
            lib_entreprise=lib_entreprise,
            siege_sociale=siege_sociale
        )
        new_gct17.save()

        return redirect('gct17_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct17_create.html')  # Display the creation form

def gct17_update(request, pk):
    gct17_item = get_object_or_404(GCT17, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_entreprise = request.POST.get('lib_entreprise')
        siege_sociale = request.POST.get('siege_sociale')

        # Update the GCT17 object
        gct17_item.lib_entreprise = lib_entreprise
        gct17_item.siege_sociale = siege_sociale
        gct17_item.save()

        return redirect('gct17_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct17_update.html', {'gct17_item': gct17_item})

def gct17_delete(request, pk):
    gct17_item = get_object_or_404(GCT17, pk=pk)

    if request.method == 'POST':
        # Delete the GCT17 object
        gct17_item.delete()
        return redirect('gct17_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct17_delete.html', {'gct17_item': gct17_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT18

def gct18_list(request):
    gct18_items = GCT18.objects.all()
    return render(request, 'gct18_list.html', {'gct18_items': gct18_items})

def gct18_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_etablissement = request.POST.get('lib_etablissement')

        # Create a new GCT18 object
        new_gct18 = GCT18.objects.create(
            lib_etablissement=lib_etablissement
        )
        new_gct18.save()

        return redirect('gct18_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct18_create.html')  # Display the creation form

def gct18_update(request, pk):
    gct18_item = get_object_or_404(GCT18, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_etablissement = request.POST.get('lib_etablissement')

        # Update the GCT18 object
        gct18_item.lib_etablissement = lib_etablissement
        gct18_item.save()

        return redirect('gct18_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct18_update.html', {'gct18_item': gct18_item})

def gct18_delete(request, pk):
    gct18_item = get_object_or_404(GCT18, pk=pk)

    if request.method == 'POST':
        # Delete the GCT18 object
        gct18_item.delete()
        return redirect('gct18_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct18_delete.html', {'gct18_item': gct18_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT19, GCT32, GCT41, GCT17

def gct19_list(request):
    gct19_items = GCT19.objects.all()
    return render(request, 'gct19_list.html', {'gct19_items': gct19_items})

def gct19_create(request):
    if request.method == 'POST':
        # Retrieve form data
        poste_id = request.POST.get('poste')
        type_contrat_id = request.POST.get('type_contrat')
        entreprise_id = request.POST.get('entreprise')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')

        # Create a new GCT19 object
        new_gct19 = GCT19.objects.create(
            poste=GCT32.objects.get(id=poste_id),
            type_contrat=GCT41.objects.get(id=type_contrat_id),
            entreprise=GCT17.objects.get(id=entreprise_id),
            date_debut=date_debut,
            date_fin=date_fin
        )
        new_gct19.save()

        return redirect('gct19_list')  # Redirect to the list after creation
    else:
        postes = GCT32.objects.all()
        types_contrat = GCT41.objects.all()
        entreprises = GCT17.objects.all()
        return render(request, 'gct19_create.html', {
            'postes': postes,
            'types_contrat': types_contrat,
            'entreprises': entreprises,
        })  # Display the creation form

def gct19_update(request, pk):
    gct19_item = get_object_or_404(GCT19, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        poste_id = request.POST.get('poste')
        type_contrat_id = request.POST.get('type_contrat')
        entreprise_id = request.POST.get('entreprise')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')

        # Update the GCT19 object
        gct19_item.poste = GCT32.objects.get(id=poste_id)
        gct19_item.type_contrat = GCT41.objects.get(id=type_contrat_id)
        gct19_item.entreprise = GCT17.objects.get(id=entreprise_id)
        gct19_item.date_debut = date_debut
        gct19_item.date_fin = date_fin
        gct19_item.save()

        return redirect('gct19_list')  # Redirect to the list after modification
    else:
        postes = GCT32.objects.all()
        types_contrat = GCT41.objects.all()
        entreprises = GCT17.objects.all()
        return render(request, 'gct19_update.html', {
            'gct19_item': gct19_item,
            'postes': postes,
            'types_contrat': types_contrat,
            'entreprises': entreprises,
        })

def gct19_delete(request, pk):
    gct19_item = get_object_or_404(GCT19, pk=pk)

    if request.method == 'POST':
        # Delete the GCT19 object
        gct19_item.delete()
        return redirect('gct19_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct19_delete.html', {'gct19_item': gct19_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT20

def gct20_list(request):
    gct20_items = GCT20.objects.all()
    return render(request, 'gct20_list.html', {'gct20_items': gct20_items})

def gct20_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT20 object
        new_gct20 = GCT20.objects.create(
            # Set your model fields with form data
        )
        new_gct20.save()

        return redirect('gct20_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct20_create.html')  # Display the creation form

def gct20_update(request, pk):
    gct20_item = get_object_or_404(GCT20, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT20 object
        # Set your model fields with form data
        gct20_item.save()

        return redirect('gct20_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct20_update.html', {'gct20_item': gct20_item})

def gct20_delete(request, pk):
    gct20_item = get_object_or_404(GCT20, pk=pk)

    if request.method == 'POST':
        # Delete the GCT20 object
        gct20_item.delete()
        return redirect('gct20_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct20_delete.html', {'gct20_item': gct20_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT21

def gct21_list(request):
    gct21_items = GCT21.objects.all()
    return render(request, 'gct21_list.html', {'gct21_items': gct21_items})

def gct21_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_genre = request.POST.get('lib_genre')

        # Create a new GCT21 object
        new_gct21 = GCT21.objects.create(
            lib_genre=lib_genre
        )
        new_gct21.save()

        return redirect('gct21_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct21_create.html')  # Display the creation form

def gct21_update(request, pk):
    gct21_item = get_object_or_404(GCT21, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_genre = request.POST.get('lib_genre')

        # Update the GCT21 object
        gct21_item.lib_genre = lib_genre
        gct21_item.save()

        return redirect('gct21_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct21_update.html', {'gct21_item': gct21_item})

def gct21_delete(request, pk):
    gct21_item = get_object_or_404(GCT21, pk=pk)

    if request.method == 'POST':
        # Delete the GCT21 object
        gct21_item.delete()
        return redirect('gct21_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct21_delete.html', {'gct21_item': gct21_item})



from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT22

def gct22_list(request):
    gct22_items = GCT22.objects.all()
    return render(request, 'gct22_list.html', {'gct22_items': gct22_items})

def gct22_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_groupe_user = request.POST.get('lib_groupe_user')

        # Create a new GCT22 object
        new_gct22 = GCT22.objects.create(
            lib_groupe_user=lib_groupe_user
        )
        new_gct22.save()

        return redirect('gct22_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct22_create.html')  # Display the creation form

def gct22_update(request, pk):
    gct22_item = get_object_or_404(GCT22, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_groupe_user = request.POST.get('lib_groupe_user')

        # Update the GCT22 object
        gct22_item.lib_groupe_user = lib_groupe_user
        gct22_item.save()

        return redirect('gct22_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct22_update.html', {'gct22_item': gct22_item})

def gct22_delete(request, pk):
    gct22_item = get_object_or_404(GCT22, pk=pk)

    if request.method == 'POST':
        # Delete the GCT22 object
        gct22_item.delete()
        return redirect('gct22_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct22_delete.html', {'gct22_item': gct22_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT23

def gct23_list(request):
    gct23_items = GCT23.objects.all()
    return render(request, 'gct23_list.html', {'gct23_items': gct23_items})

def gct23_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT23 object
        new_gct23 = GCT23.objects.create(
            # Set your model fields with form data
        )
        new_gct23.save()

        return redirect('gct23_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct23_create.html')  # Display the creation form

def gct23_update(request, pk):
    gct23_item = get_object_or_404(GCT23, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT23 object
        # Set your model fields with form data
        gct23_item.save()

        return redirect('gct23_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct23_update.html', {'gct23_item': gct23_item})

def gct23_delete(request, pk):
    gct23_item = get_object_or_404(GCT23, pk=pk)

    if request.method == 'POST':
        # Delete the GCT23 object
        gct23_item.delete()
        return redirect('gct23_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct23_delete.html', {'gct23_item': gct23_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT24

def gct24_list(request):
    gct24_items = GCT24.objects.all()
    return render(request, 'gct24_list.html', {'gct24_items': gct24_items})

def gct24_create(request):
    if request.method == 'POST':
        # Retrieve form data
        lib_loisirs = request.POST.get('lib_loisirs')

        # Create a new GCT24 object
        new_gct24 = GCT24.objects.create(
            lib_loisirs=lib_loisirs
        )
        new_gct24.save()

        return redirect('gct24_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct24_create.html')  # Display the creation form

def gct24_update(request, pk):
    gct24_item = get_object_or_404(GCT24, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        lib_loisirs = request.POST.get('lib_loisirs')

        # Update the GCT24 object
        gct24_item.lib_loisirs = lib_loisirs
        gct24_item.save()

        return redirect('gct24_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct24_update.html', {'gct24_item': gct24_item})

def gct24_delete(request, pk):
    gct24_item = get_object_or_404(GCT24, pk=pk)

    if request.method == 'POST':
        # Delete the GCT24 object
        gct24_item.delete()
        return redirect('gct24_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct24_delete.html', {'gct24_item': gct24_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT25

def gct25_list(request):
    gct25_items = GCT25.objects.all()
    return render(request, 'gct25_list.html', {'gct25_items': gct25_items})

def gct25_create(request):
    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        diplome_id = request.POST.get('diplome')
        date = request.POST.get('date')

        # Create a new GCT25 object
        new_gct25 = GCT25.objects.create(
            candidat=GCT07.objects.get(id=candidat_id),
            diplome=GCT13.objects.get(id=diplome_id),
            date=date
        )
        new_gct25.save()

        return redirect('gct25_list')  # Redirect to the list after creation
    else:
        candidats = GCT07.objects.all()
        diplomes = GCT13.objects.all()
        return render(request, 'gct25_create.html', {'candidats': candidats, 'diplomes': diplomes})

def gct25_update(request, pk):
    gct25_item = get_object_or_404(GCT25, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        diplome_id = request.POST.get('diplome')
        date = request.POST.get('date')

        # Update the GCT25 object
        gct25_item.candidat = GCT07.objects.get(id=candidat_id)
        gct25_item.diplome = GCT13.objects.get(id=diplome_id)
        gct25_item.date = date
        gct25_item.save()

        return redirect('gct25_list')  # Redirect to the list after modification
    else:
        candidats = GCT07.objects.all()
        diplomes = GCT13.objects.all()
        return render(request, 'gct25_update.html', {'gct25_item': gct25_item, 'candidats': candidats, 'diplomes': diplomes})

def gct25_delete(request, pk):
    gct25_item = get_object_or_404(GCT25, pk=pk)

    if request.method == 'POST':
        # Delete the GCT25 object
        gct25_item.delete()
        return redirect('gct25_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct25_delete.html', {'gct25_item': gct25_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT26

def gct26_list(request):
    gct26_items = GCT26.objects.all()
    return render(request, 'gct26_list.html', {'gct26_items': gct26_items})

def gct26_create(request):
    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        poste_id = request.POST.get('poste')
        date = request.POST.get('date')

        # Create a new GCT26 object
        new_gct26 = GCT26.objects.create(
            candidat=GCT07.objects.get(id=candidat_id),
            poste=GCT32.objects.get(id=poste_id),
            date=date
        )
        new_gct26.save()

        return redirect('gct26_list')  # Redirect to the list after creation
    else:
        candidats = GCT07.objects.all()
        postes = GCT32.objects.all()
        return render(request, 'gct26_create.html', {'candidats': candidats, 'postes': postes})

def gct26_update(request, pk):
    gct26_item = get_object_or_404(GCT26, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        candidat_id = request.POST.get('candidat')
        poste_id = request.POST.get('poste')
        date = request.POST.get('date')

        # Update the GCT26 object
        gct26_item.candidat = GCT07.objects.get(id=candidat_id)
        gct26_item.poste = GCT32.objects.get(id=poste_id)
        gct26_item.date = date
        gct26_item.save()

        return redirect('gct26_list')  # Redirect to the list after modification
    else:
        candidats = GCT07.objects.all()
        postes = GCT32.objects.all()
        return render(request, 'gct26_update.html', {'gct26_item': gct26_item, 'candidats': candidats, 'postes': postes})

def gct26_delete(request, pk):
    gct26_item = get_object_or_404(GCT26, pk=pk)

    if request.method == 'POST':
        # Delete the GCT26 object
        gct26_item.delete()
        return redirect('gct26_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct26_delete.html', {'gct26_item': gct26_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT27

def gct27_list(request):
    gct27_items = GCT27.objects.all()
    return render(request, 'gct27_list.html', {'gct27_items': gct27_items})

def gct27_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT27 object
        new_gct27 = GCT27.objects.create(
            # Set your model fields with form data
        )
        new_gct27.save()

        return redirect('gct27_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct27_create.html')  # Display the creation form

def gct27_update(request, pk):
    gct27_item = get_object_or_404(GCT27, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT27 object
        # Set your model fields with form data
        gct27_item.save()

        return redirect('gct27_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct27_update.html', {'gct27_item': gct27_item})

def gct27_delete(request, pk):
    gct27_item = get_object_or_404(GCT27, pk=pk)

    if request.method == 'POST':
        # Delete the GCT27 object
        gct27_item.delete()
        return redirect('gct27_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct27_delete.html', {'gct27_item': gct27_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT28

def gct28_list(request):
    gct28_items = GCT28.objects.all()
    return render(request, 'gct28_list.html', {'gct28_items': gct28_items})

def gct28_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT28 object
        new_gct28 = GCT28.objects.create(
            # Set your model fields with form data
        )
        new_gct28.save()

        return redirect('gct28_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct28_create.html')  # Display the creation form

def gct28_update(request, pk):
    gct28_item = get_object_or_404(GCT28, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT28 object
        # Set your model fields with form data
        gct28_item.save()

        return redirect('gct28_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct28_update.html', {'gct28_item': gct28_item})

def gct28_delete(request, pk):
    gct28_item = get_object_or_404(GCT28, pk=pk)

    if request.method == 'POST':
        # Delete the GCT28 object
        gct28_item.delete()
        return redirect('gct28_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct28_delete.html', {'gct28_item': gct28_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT29

def gct29_list(request):
    gct29_items = GCT29.objects.all()
    return render(request, 'gct29_list.html', {'gct29_items': gct29_items})

def gct29_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT29 object
        new_gct29 = GCT29.objects.create(
            # Set your model fields with form data
        )
        new_gct29.save()

        return redirect('gct29_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct29_create.html')  # Display the creation form

def gct29_update(request, pk):
    gct29_item = get_object_or_404(GCT29, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT29 object
        # Set your model fields with form data
        gct29_item.save()

        return redirect('gct29_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct29_update.html', {'gct29_item': gct29_item})

def gct29_delete(request, pk):
    gct29_item = get_object_or_404(GCT29, pk=pk)

    if request.method == 'POST':
        # Delete the GCT29 object
        gct29_item.delete()
        return redirect('gct29_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct29_delete.html', {'gct29_item': gct29_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT30

def gct30_list(request):
    gct30_items = GCT30.objects.all()
    return render(request, 'gct30_list.html', {'gct30_items': gct30_items})

def gct30_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT30 object
        new_gct30 = GCT30.objects.create(
            # Set your model fields with form data
        )
        new_gct30.save()

        return redirect('gct30_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct30_create.html')  # Display the creation form

def gct30_update(request, pk):
    gct30_item = get_object_or_404(GCT30, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT30 object
        # Set your model fields with form data
        gct30_item.save()

        return redirect('gct30_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct30_update.html', {'gct30_item': gct30_item})

def gct30_delete(request, pk):
    gct30_item = get_object_or_404(GCT30, pk=pk)

    if request.method == 'POST':
        # Delete the GCT30 object
        gct30_item.delete()
        return redirect('gct30_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct30_delete.html', {'gct30_item': gct30_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT31

def gct31_list(request):
    gct31_items = GCT31.objects.all()
    return render(request, 'gct31_list.html', {'gct31_items': gct31_items})

def gct31_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT31 object
        new_gct31 = GCT31.objects.create(
            # Set your model fields with form data
        )
        new_gct31.save()

        return redirect('gct31_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct31_create.html')  # Display the creation form

def gct31_update(request, pk):
    gct31_item = get_object_or_404(GCT31, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT31 object
        # Set your model fields with form data
        gct31_item.save()

        return redirect('gct31_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct31_update.html', {'gct31_item': gct31_item})

def gct31_delete(request, pk):
    gct31_item = get_object_or_404(GCT31, pk=pk)

    if request.method == 'POST':
        # Delete the GCT31 object
        gct31_item.delete()
        return redirect('gct31_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct31_delete.html', {'gct31_item': gct31_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT32

def gct32_list(request):
    gct32_items = GCT32.objects.all()
    return render(request, 'gct32_list.html', {'gct32_items': gct32_items})

def gct32_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT32 object
        new_gct32 = GCT32.objects.create(
            # Set your model fields with form data
        )
        new_gct32.save()

        return redirect('gct32_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct32_create.html')  # Display the creation form

def gct32_update(request, pk):
    gct32_item = get_object_or_404(GCT32, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT32 object
        # Set your model fields with form data
        new_gct32.save()

        return redirect('gct32_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct32_update.html', {'gct32_item': gct32_item})

def gct32_delete(request, pk):
    gct32_item = get_object_or_404(GCT32, pk=pk)

    if request.method == 'POST':
        # Delete the GCT32 object
        gct32_item.delete()
        return redirect('gct32_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct32_delete.html', {'gct32_item': gct32_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT33

def gct33_list(request):
    gct33_items = GCT33.objects.all()
    return render(request, 'gct33_list.html', {'gct33_items': gct33_items})

def gct33_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT33 object
        new_gct33 = GCT33.objects.create(
            # Set your model fields with form data
        )
        new_gct33.save()

        return redirect('gct33_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct33_create.html')  # Display the creation form

def gct33_update(request, pk):
    gct33_item = get_object_or_404(GCT33, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT33 object
        # Set your model fields with form data
        gct33_item.save()

        return redirect('gct33_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct33_update.html', {'gct33_item': gct33_item})

def gct33_delete(request, pk):
    gct33_item = get_object_or_404(GCT33, pk=pk)

    if request.method == 'POST':
        # Delete the GCT33 object
        gct33_item.delete()
        return redirect('gct33_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct33_delete.html', {'gct33_item': gct33_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT34

def gct34_list(request):
    gct34_items = GCT34.objects.all()
    return render(request, 'gct34_list.html', {'gct34_items': gct34_items})

def gct34_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT34 object
        new_gct34 = GCT34.objects.create(
            # Set your model fields with form data
        )
        new_gct34.save()

        return redirect('gct34_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct34_create.html')  # Display the creation form

def gct34_update(request, pk):
    gct34_item = get_object_or_404(GCT34, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT34 object
        # Set your model fields with form data
        gct34_item.save()

        return redirect('gct34_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct34_update.html', {'gct34_item': gct34_item})

def gct34_delete(request, pk):
    gct34_item = get_object_or_404(GCT34, pk=pk)

    if request.method == 'POST':
        # Delete the GCT34 object
        gct34_item.delete()
        return redirect('gct34_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct34_delete.html', {'gct34_item': gct34_item})


from django.shortcuts import render, get_object_or_404, redirect
from .models import GCT35

def gct35_list(request):
    gct35_items = GCT35.objects.all()
    return render(request, 'gct35_list.html', {'gct35_items': gct35_items})

def gct35_create(request):
    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Create a new GCT35 object
        new_gct35 = GCT35.objects.create(
            # Set your model fields with form data
        )
        new_gct35.save()

        return redirect('gct35_list')  # Redirect to the list after creation
    else:
        return render(request, 'gct35_create.html')  # Display the creation form

def gct35_update(request, pk):
    gct35_item = get_object_or_404(GCT35, pk=pk)

    if request.method == 'POST':
        # Retrieve form data
        # Add your form fields here

        # Update the GCT35 object
        # Set your model fields with form data
        gct35_item.save()

        return redirect('gct35_list')  # Redirect to the list after modification
    else:
        return render(request, 'gct35_update.html', {'gct35_item': gct35_item})

def gct35_delete(request, pk):
    gct35_item = get_object_or_404(GCT35, pk=pk)

    if request.method == 'POST':
        # Delete the GCT35 object
        gct35_item.delete()
        return redirect('gct35_list')  # Redirect to the list after deletion
    else:
        return render(request, 'gct35_delete.html', {'gct35_item': gct35_item})


