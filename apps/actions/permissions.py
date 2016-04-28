from rest_framework import permissions
from apps.actions.models import TypeAction


class ActionPermission(permissions.BasePermission):
    """
    Definit les permissions pour les actions
    """
    # TODO:changer les parametres de actions une action doit elle correspondre a un type d'action necessairement ?
    # def has_permission(self, request, view):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     elif request.method == "POST":
    #         if permissions.IsAuthenticated.has_permission(self,request,view):
    #             if "nom" in request.data:
    #                 if TypeAction.objects.get(nom=request.data["nom"]):
    #                     return True
    #             # pour permettre le test de l'api
    #             else:
    #                 return True
    #     else:
    #         return False
