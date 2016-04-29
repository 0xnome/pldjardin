from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from apps.gensdujardin.models import Profil


def content_file_name_jardin(instance, filename):
    """
    Chemin pour l'image du jadin
    Args:
        instance:
        filename:

    Returns:

    """
    return '/'.join(['images-jardins', instance.nom + instance.adresse.ville, filename])


def content_file_name_plante(instance, filename):
    return '/'.join(['plantes', instance.nom + instance.lopin.adresse.ville, filename])


class Adresse(models.Model):
    ville = models.CharField(max_length=100)
    code_postal_regex = RegexValidator(regex=r'^\d{5}$',
                                       message="Le numéro de téléphone doit être composé de 10 chiffres.")
    code_postal = models.CharField(max_length=5, validators=[code_postal_regex], verbose_name="Code postal")
    rue = models.CharField(max_length=200)
    long = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)

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
    description = models.TextField(blank=True, null=True)
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
                                help_text="Adresse du lopin. Cette adresse doit être égale à l'adresse du jardin si le lopin se trouve dans un jardin")
    jardin = models.ForeignKey(Jardin, on_delete=models.CASCADE, null=True, related_name='lopins')
    nom = models.CharField(max_length=50, help_text="Nom du lopin")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.nom, self.description)


class Plante(models.Model):
    lopin = models.ForeignKey(Lopin, on_delete=models.CASCADE, related_name="plantes")

    nom = models.CharField(max_length=30, help_text="Nom commun de la plante", verbose_name="Nom de la plante")
    # TODO default pour l'image, calcul en fonction de l'espce ?
    image = models.ImageField(upload_to=content_file_name_plante, null=True)
    espece = models.CharField(max_length=50, help_text="Nom scientifique de la plante")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.nom, self.description)
