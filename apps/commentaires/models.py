from django.db import models


# Create your models here.
class Commentaire(models.Model):
    texte = models.TextField(blank=False, null=False)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création",
                                         help_text="Date de création du commentaire")
    utilisateur = models.ForeignKey('gensdujardin.Utilisateur', on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ['date_creation']


class CommentairePlante(Commentaire):
    plante = models.ForeignKey('jardin.Plante', on_delete=models.CASCADE)


class CommentaireJardin(Commentaire):
    jardin = models.ForeignKey('jardin.Jardin', on_delete=models.CASCADE)


class CommentaireLopin(Commentaire):
    lopin = models.ForeignKey('jardin.Lopin', on_delete=models.CASCADE)
