from django.contrib.auth.models import User
from django.db import models


class Commentaire(models.Model):
    texte = models.TextField(blank=False, null=False)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création",
                                         help_text="Date de création du commentaire")
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ['date_creation']


class CommentairePlante(Commentaire):
    plante = models.ForeignKey('jardin.Plante', on_delete=models.CASCADE, related_name="commentaires")


class CommentaireJardin(Commentaire):
    jardin = models.ForeignKey('jardin.Jardin', on_delete=models.CASCADE, related_name="commentaires")


class CommentaireLopin(Commentaire):
    lopin = models.ForeignKey('jardin.Lopin', on_delete=models.CASCADE, related_name="commentaires")
