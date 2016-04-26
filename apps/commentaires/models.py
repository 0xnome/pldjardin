from django.db import models



# Create your models here.

class CommentairePlante(models.Model):
  texte = models.TextField(blank = False, null = False)
  datetime = models.DateTimeField( auto_now_add = True )
  utilisateur = models.ForeignKey(
    'gensdujardin.Utilisateur',
    on_delete = models.CASCADE
  )
  plante = models.ForeignKey(
    'jardin.Plante',
    on_delete = models.CASCADE
  )

class CommentaireJardin(models.Model):
  texte = models.TextField(blank = False, null = False)
  datetime = models.DateTimeField( auto_now_add = True )
  utilisateur = models.ForeignKey(
    'gensdujardin.Utilisateur',
    on_delete = models.CASCADE
  )
  jardin = models.ForeignKey(
    'jardin.Jardin',
    on_delete = models.CASCADE
  )

class CommentaireLopin(models.Model):
  texte = models.TextField(blank = False, null = False)
  datetime = models.DateTimeField( auto_now_add = True )
  utilisateur = models.ForeignKey(
    'gensdujardin.Utilisateur',
    on_delete = models.CASCADE
  )
  lopin = models.ForeignKey(
    'jardin.Lopin',
    on_delete = models.CASCADE
  )