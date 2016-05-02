from django.contrib.auth.models import User
from django.db import models

from apps.jardin.models import Lopin, Plante


class Action(models.Model):
    ARROSER = 'AR'
    PLANTER = 'PL'
    RETIRER = 'RE'
    CUEILLIR = 'CE'
    FERTILISER = 'FE'
    ELAGUER = 'EL'
    #LIBRE = 'LI'
    ALL_ACTION = (
        (ARROSER, 'Arroser'),
        (PLANTER, 'Planter'),
        (RETIRER, 'Retirer'),
        (CUEILLIR, 'Cueillir'),
        (FERTILISER, 'Fertiliser'),
        (ELAGUER, 'Elaguer'),
        # (LIBRE, 'Libre')
    )
    USER_AVAILABLE_ACTION =(ARROSER, CUEILLIR, FERTILISER, ELAGUER,)

    type = models.CharField(max_length=2,choices=ALL_ACTION)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actions")
    # lopin = models.ForeignKey(Lopin, on_delete=models.CASCADE, null=True, related_name="actions")
    plante = models.ForeignKey(Plante, on_delete=models.CASCADE,  null=True, related_name="actions")
    date_creation = models.DateTimeField(auto_now_add=True, help_text="Date de création de l'action",
                                         verbose_name="Date de création")

    def __str__(self):
        if self.type == self.ARROSER:
            # un UTILISATEUR arrose une PLANTE
            return "{} a arrosé la plante {}".format(self.utilisateur.username, self.plante.nom)
        elif self.type == self.PLANTER:
            # un UTILISATEUR plante une PLANTE
            return "{} a planté la plante {}".format(self.utilisateur.username, self.plante.nom)
        elif self.type == self.CUEILLIR:
            # un UTILISATEUR cueille une PLANTE
            return "{} a cueilli la plante {}".format(self.utilisateur.username, self.plante.nom)
        elif self.type == self.FERTILISER:
            # un UTILISATEUR cueille une PLANTE
            return "{} a fertilisé la plante {}".format(self.utilisateur.username, self.plante.nom)
        elif self.type == self.ELAGUER:
            return "{} a élagué la plante {}".format(self.utilisateur.username, self.plante.nom)
        return "Action inconnue : {}".format(self.type)
