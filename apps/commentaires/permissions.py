from rest_framework import permissions

from apps.jardin.models import Jardin


class CommentaireJardinPermission(permissions.BasePermission):
    """
    Global permissions for ActualiteJardin
    """
    def has_object_permission(self, request, view, obj):
        # get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        # utilisateur connecté
        elif permissions.IsAuthenticated:
            if request.method == "DELETE":
                if request.user == obj.auteur:
                    return True
                elif request.user in obj.jardin.administrateurs.all():
                    return True
        return False

    def has_permission(self, request, view):
        # get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        # utilisateur connecté
        elif permissions.IsAuthenticated.has_permission(self,request,view):
            if request.method == "POST":
                if "jardin" in request.data:
                    id = int(request.data["jardin"])
                    # jardin non restreint
                    if not (Jardin.objects.get(pk=id).restreint):
                        return True
                    # utilisateur membre du jardin restreint
                    elif request.user in Jardin.objects.get(pk=id).membres.all():
                        return True
                # pour le test de l'api rest
                else:
                    return True
            #  DELETE PUT PATCH
            else:
                return True
        # l'utilisateur non connecté n'a pas de droit de modification
        return False
