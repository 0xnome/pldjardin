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
    ALL_ACTION = (
        (ARROSER, 'Arroser'),
        (PLANTER, 'Planter'),
        (RETIRER, 'Retirer'),
        (CUEILLIR, 'Cueillir'),
        (FERTILISER, 'Fertiliser'),
        (ELAGUER, 'Elaguer')
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
            pass
        elif self.type == self.PLANTER:
            # un UTILISATEUR plante une PLANTE
            pass
        elif self.type == self.CUEILLIR:
            # un UTILISATEUR cueille une PLANTE
            pass
        elif self.type == self.FERTILISER:
            # un UTILISATEUR cueille une PLANTE
            pass
        elif self.type == self.ELAGUER:
            pass
        return "Action inconnue : {}".format(self.type)
