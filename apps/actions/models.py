from django.db import models


# Create your models here.
class TypeAction(models.Model):
    nom = models.CharField(max_length=100, help_text="Nom de l'action")

    def __str__(self):
        return "{}".format(self.nom)


class Action(models.Model):
    type_action = models.ForeignKey(TypeAction)
    utilisateur = models.ForeignKey('gensdujardin.Profil', on_delete=models.CASCADE)
    lopin = models.ForeignKey('jardin.Lopin', on_delete=models.CASCADE)
    plante = models.ForeignKey('jardin.Plante', on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True, help_text="Date de création de l'action",
                                         verbose_name="Date de création")

    def __str__(self):
        if self.lopin is None:
            return "{} le {} par {} sur {}".format(self.type_action.nom, self.date_creation,
                                                   self.utilisateur.user.username, self.plante)
        else:
            return "{} le {} par {} sur {}".format(self.type_action.nom, self.date_creation,
                                                   self.utilisateur.user.username, self.lopin)
