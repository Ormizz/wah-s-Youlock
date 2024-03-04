from django.db import models

# Create your models here.

class GCT08(models.Model):
    denomination_sociale = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.denomination_sociale

class GCT14(models.Model):
    
    date = models.CharField(max_length=200)
   
    def __str__(self):
        return self.date
    
class GCT01(models.Model):
    num_abonnement = models.CharField(max_length=100)
    date_debut_abonnement = models.CharField(max_length=200)
    date_fin_abonnement = models.CharField(max_length=200)


    def __str__(self):
        return self.num_abonnement
    
class GCT16(models.Model):
    nom_employe = models.CharField(max_length=100)
    prenom_employe = models.CharField(max_length=200)
    date_naissance = models.CharField(max_length=15)
    adresse = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nom_employe

class GCT24(models.Model):
    libelle_loisirs = models.CharField(max_length=200)

    def __str__(self):
        return self.libelle_loisirs
    
class GCT42(models.Model):
    nom_utlisateur = models.CharField(max_length=200)
    prenom_utilisateur = models.CharField(max_length=200)
    date_naissance_user = models.CharField(max_length=15)
    adresse_user = models.CharField(max_length=15)
    telephone_user = models.CharField(max_length=15)
    email_user = models.EmailField()

    def __str__(self):
        return self.nom_utlisateur
    
class GCT39(models.Model):
    intitule_test_psycho = models.CharField(max_length=100)

    def __str__(self):
        return self.intitule_test_psycho
    
class GCT29(models.Model):
    lib_pays = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_pays
    
class GCT50(models.Model):
    lib_question = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_question
    
class GCT54(models.Model):
    lib_type_utilisateur = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_type_utilisateur

class GCT22(models.Model):
    lib_groupe_user = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_groupe_user 
    
class GCT32(models.Model):
    lib_poste = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_poste

class GCT24(models.Model):
    lib_loisirs = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_loisirs

class GCT50(models.Model):
    lib_question = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_question
    
class GCT35(models.Model):
    lib_entretien = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_entretien
    

class GCT34(models.Model):
    
    lib_profession = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_profession
    
class GCT41(models.Model):
    lib_type_contrat = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_type_contrat
    
class GCT40(models.Model):
    lib_traitement = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_traitement
    
class GCT13(models.Model):
    lib_diplome = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_diplome
    
class GCT38(models.Model):
    lib_specialite = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_specialite

class GCT17(models.Model):
    lib_entreprise = models.CharField(max_length=100)
    siege_sociale = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_entreprise
    
class GCT03(models.Model):
    lib_appel_offre = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_appel_offre

class GCT21(models.Model):
    lib_genre = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_genre

class GCT18(models.Model):
    lib_etablissement = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_etablissement
    
class GCT07(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class GCT31(models.Model):
    lib_piece_identite = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_piece_identite
    
class GCT11(models.Model):
    lib_diplome = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_diplome

class GCT55(models.Model):
    lib_competences = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_competences

class GCT46(models.Model):
    lib_entretien = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_entretien

class GCT45(models.Model):
    lib_niveau_access = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_niveau_access
    
class GCT37(models.Model):
    lib_situation_matrimoniale = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_situation_matrimoniale
    
class GCT52(models.Model):
    lib_type_test = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_type_test
    
class GCT51(models.Model):
    lib_type_question = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_type_question
    
class GCT43(models.Model):
    lib_type_question = models.CharField(max_length=100)
    # à completer

    def __str__(self):
        return self.lib_type_question

class GCT09(models.Model):
    lib_compte_comptable = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_compte_comptable
    
class GCT02(models.Model):
    lib_action = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_action
    
class GCT51(models.Model):
    lib_type_question = models.CharField(max_length=100)

    def __str__(self):
        return self.lib_type_question
    
class GCT04(models.Model):
    candidat = models.ForeignKey(GCT07, on_delete=models.CASCADE)
    situatiion_matrimoniale = models.ForeignKey(GCT37, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Le candidat {self.candidat} est {self.situatiion_matrimoniale} à la date du {self.date}"
    
class GCT05(models.Model):
    candidat = models.ForeignKey(GCT07, on_delete=models.CASCADE)
    specialite = models.ForeignKey(GCT38, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Le candidat {self.candidat} a acquis cette {self.specialite} à la date du {self.date}"
    
class GCT10(models.Model):
    utilisateur = models.ForeignKey(GCT42, on_delete=models.CASCADE)
    traitement = models.ForeignKey(GCT40, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Le candidat {self.utilisateur} a {self.traitement} à la date du {self.date}"
    
class GCT14(models.Model):
    candidat = models.ForeignKey(GCT07, on_delete=models.CASCADE)
    entretien = models.ForeignKey(GCT46, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Le candidat {self.candidat} a eu un entretien {self.entretien} à la date du {self.date}"
    
class GCT15(models.Model):
    candidat = models.ForeignKey(GCT07, on_delete=models.CASCADE)
    test = models.ForeignKey(GCT39, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Le candidat {self.candidat} a fait {self.test} à la date du {self.date}"
    
class GCT20(models.Model):
    utilisateur = models.ForeignKey(GCT42, on_delete=models.CASCADE)
    appel_offre = models.ForeignKey(GCT03, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return f"L'utilisateur {self.utilisateur} a fait {self.appel_offre} à la date du {self.date}"
    
class GCT25(models.Model):
    candidat = models.ForeignKey(GCT07, on_delete=models.CASCADE)
    diplome = models.ForeignKey(GCT13, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Le candidat {self.candidat} a {self.diplome} à la date du {self.date}"
    
class GCT26(models.Model):
    candidat = models.ForeignKey(GCT07, on_delete=models.CASCADE)
    poste = models.ForeignKey(GCT32, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Le candidat {self.candidat} a acquis le poste {self.poste} à la date du {self.date}"
    
class GCT27(models.Model):
    candidat = models.ForeignKey(GCT07, on_delete=models.CASCADE)
    specialite = models.ForeignKey(GCT38, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Le candidat {self.candidat} a acquis cette {self.specialite} à la date du {self.date}"