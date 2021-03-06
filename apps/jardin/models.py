import os

import io
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models, transaction
from django.utils.text import slugify

from apps.gensdujardin.models import Profil


def content_file_name_jardin(jardin, filename):
    return os.path.join(*['jardins', str(jardin.pk) + "_" + slugify(jardin.nom), filename])


def content_file_name_plante(plante, filename):
    return os.path.join(*['plantes', str(plante.pk) + "_" + slugify(plante.nom), filename])


class Adresse(models.Model):
    ville = models.CharField(max_length=100)
    code_postal_regex = RegexValidator(regex=r'^\d{5}$',
                                       message="Le code postal doit être composé de 5 chiffres.")
    code_postal = models.CharField(max_length=5, validators=[code_postal_regex], verbose_name="Code postal")
    rue = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=7, default=0.0, blank=True, null=True)
    long = models.DecimalField(max_digits=9, decimal_places=7, default=0.0, blank=True, null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.rue, self.ville, self.code_postal)


def create_default_adresse():
    return Adresse(ville="Villeurbane", rue="20 avenue Albert Einstein", code_postal='69100')


class Jardin(models.Model):
    adresse = models.ForeignKey(Adresse, related_name="jardins")
    administrateurs = models.ManyToManyField(User, related_name="admin_jardins")
    membres = models.ManyToManyField(User, related_name="membre_jardins")

    nom = models.CharField(max_length=50, help_text="Nom du jardin")
    site = models.CharField(max_length=200, help_text="Le site web du jardin", blank=True, null=True)
    contact = models.EmailField(help_text="Email de contact du jardin, ou le mail d'un responsable")
    horaire = models.TextField()
    # TODO mettre une image par defaut a la place du null false
    image = models.ImageField(upload_to=content_file_name_jardin, null=True)
    plan = models.ImageField(upload_to=content_file_name_jardin, null=True)
    description = models.TextField(blank=True, null=True, default="Pas de description")
    restreint = models.BooleanField(default=False)
    composteur = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.nom, self.adresse.ville)


class Actualite(models.Model):
    jardin = models.ForeignKey(Jardin, on_delete=models.CASCADE, related_name="actualites")
    auteur = models.ForeignKey(User)
    texte = models.TextField(blank=False, null=False)
    date_creation = models.DateTimeField(help_text="Date de création", verbose_name="Date de création",
                                         auto_now_add=True)

    def __str__(self):
        return "Actualité liée au jardin {}. Créee le {}".format(self.jardin.nom, self.date_creation)


class Lopin(models.Model):
    adresse = models.ForeignKey(Adresse,related_name="lopins",
                                help_text="Adresse du lopin indépendant.",
                                null=True)
    jardin = models.ForeignKey(Jardin, on_delete=models.CASCADE, null=True, related_name='lopins')

    nom = models.CharField(max_length=50, help_text="Nom du lopin")
    description = models.TextField(blank=True, null=True, default="Pas de description")

    def __str__(self):
        j = str(self.jardin.pk) if self.jardin else None
        return "{} - {}".format(self.nom, self.description)


class Plante(models.Model):
    lopin = models.ForeignKey(Lopin, on_delete=models.CASCADE, related_name="plantes")

    nom = models.CharField(max_length=30, help_text="Nom commun de la plante", verbose_name="Nom de la plante")
    # TODO default pour l'image, calcul en fonction de l'espce ?
    image = models.ImageField(upload_to=content_file_name_plante, null=True)
    espece = models.CharField(max_length=50, help_text="Nom scientifique de la plante")
    description = models.TextField(null=True, blank=True, default="Pas de description")

    def __str__(self):
        return "{} - {}".format(self.nom, self.description)

class PlanteInfo(models.Model):
    commun = models.CharField(max_length=200, verbose_name="Le nom commun de la plante")
    scientifique = models.CharField(max_length=200, verbose_name="Le nom scientifique de la plante")

    def __str__(self):
        return "{} ({})".format(self.commun, self.scientifique)

@transaction.atomic()
def loadPlantes():
    import csv
    filename = 'doc/base_plante.csv'
    with io.open(filename,'r',encoding='utf8') as file:
        data = csv.reader(file, delimiter=";")
        count = 0
        for i, row in enumerate(data):
            can_insert = True
            for j, col in enumerate(row):
                if col == "":
                    can_insert = False
            if can_insert:
                # on a toutes les infos
                PlanteInfo.objects.create(commun=row[2], scientifique=row[1])
                count += 1
            if count%100 == 0:
                print(str(count)+"/9469 PlanteInfo créées")
        print("TOTAL : "+str(count)+"/9469 PlanteInfo créées")

