from django.db import models


# Create your models here.

def content_file_name(instance, filename):
    return '/'.join(['images-jardins', instance.nom + instance.ville, filename])


class Jardin(models.Model):
    nom = models.CharField(max_length=20, help_text="Nom de la ville où se trouve le jardin")
    ville = models.CharField(max_length=20)
    code_postal = models.IntegerField(verbose_name="Code postal")
    rue = models.CharField(max_length=20)
    horaire = models.TextField()
    image = models.ImageField(upload_to=content_file_name, null=False)
    description = models.TextField(blank=True, null=True)
    restreint = models.BooleanField()
    # TODO : ajouter les coordonées GPS : latitude, longitude

    def __str__(self):
        return "{} - {} - {}".format(self.nom, self.ville, self.description)
