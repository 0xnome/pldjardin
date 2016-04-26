from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

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
    return '/'.join(['images-jardins/plantes', instance.nom + instance.lopin.adresse.ville, filename])


class Adresse(models.Model):
    ville = models.CharField(max_length=100)
    code_postal_regex = RegexValidator(regex=r'^\d{5}$',
                                       message="Le numéro de téléphone doit être composé de 10 chiffres.")
    code_postal = models.CharField(max_length=5, validators=[code_postal_regex], verbose_name="Code postal")
    rue = models.CharField(max_length=200)
    long = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)


def create_default_adresse():
    return Adresse(ville="Villeurbane", rue="20 avenue Albert Einstein", code_postal='69100')


class Jardin(models.Model):
    adresse = models.ForeignKey(Adresse)
    nom = models.CharField(max_length=30, help_text="Nom de la ville où se trouve le jardin")
    horaire = models.TextField(blank=False)
    image = models.ImageField(upload_to=content_file_name_jardin, null=False)
    description = models.TextField(blank=True, null=True)
    restreint = models.BooleanField()

    def __str__(self):
        return "{} - {} - {}".format(self.nom, self.adresse.ville, self.description)


class Actualite(models.Model):
    jardin = models.ForeignKey(Jardin, on_delete=models.CASCADE)
    texte = models.TextField(blank=False)
    date_creation = models.DateTimeField(help_text="Date de création", verbose_name="Date de création",
                                         auto_now_add=True)

    def __str__(self):
        return "Actualité lié au jardin {}. Créee le {}".format(self.jardin.nom, self.date_creation)


class Lopin(models.Model):
    adresse = models.ForeignKey(Adresse,
                                help_text="Adresse du lopin. Cette adresse doit être égale à l'adresse du jardin si le lopin se trouve dans un jardin")
    jardin = models.ForeignKey(Jardin, on_delete=models.CASCADE, null=True)
    nom = models.CharField(max_length=30, help_text="Nom du lopin")
    description = models.TextField(blank=True, null=True)


class Plante(models.Model):
    lopin = models.ForeignKey(Lopin, on_delete=models.CASCADE)
    nom = models.CharField(max_length=30, help_text="Nom de la plante", verbose_name="Nom de la plante")
    image = models.ImageField(upload_to=content_file_name_plante, null=False)
    espece = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
