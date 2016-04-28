from rest_framework import permissions

from apps.jardin.models import Jardin, Lopin, Plante


class CommentaireJardinPermission(permissions.BasePermission):
    """
    Global permissions for CommentaireJardin
    """
    def has_object_permission(self, request, view, obj):
        # get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        # utilisateur connecté
        elif permissions.IsAuthenticated.has_permission(self,request,view):
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


class CommentaireLopinPermission(permissions.BasePermission):
    """
       Global permissions for CommentaireLopin
    """
    def has_object_permission(self, request, view, obj):
        # get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        # utilisateur connecté
        elif permissions.IsAuthenticated.has_permission(self,request,view):
            if request.method == "DELETE":
                if request.user == obj.auteur:
                    return True
                elif obj.lopin.jardin:
                    if request.user in obj.jardin.administrateurs.all():
                        return True
                return False
        return False

    def has_permission(self, request, view):
        # get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        # utilisateur connecté
        elif permissions.IsAuthenticated.has_permission(self, request, view):
            if request.method == "POST":
                if "lopin" in request.data:
                    jardin = Lopin.objects.get(pk=int(request.data["lopin"])).jardin
                    if jardin:
                        if not jardin.restreint:
                            return True
                        elif request.user in jardin.membres.all():
                            return True
                    # un utilisateur peut commenter un lopin sans jardin
                    else:
                        return True

                # pour le test de l'api rest
                else:
                    return True
            # DELETE PUT PATCH
            else:
                return True
        # l'utilisateur non connecté n'a pas de droit de modification
        return False


class CommentairePlantePermission(permissions.BasePermission):
    """
       Global permissions for CommentairePlante
    """
    def has_object_permission(self, request, view, obj):
        # get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        # utilisateur connecté
        elif permissions.IsAuthenticated.has_permission(self, request, view):
            if request.method == "DELETE":
                if request.user == obj.auteur:
                    return True
                elif obj.plante.lopin.jardin:
                    if request.user in obj.plante.lopin.jardin.administrateurs.all():
                        return True
                return False
        return False

    def has_permission(self, request, view):
        # get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        # utilisateur connecté
        elif permissions.IsAuthenticated.has_permission(self, request, view):
            if request.method == "POST":
                if "plante" in request.data:
                    jardin = Plante.objects.get(pk=int(request.data["plante"])).lopin.jardin
                    if jardin:
                        if not jardin.restreint:
                            return True
                        elif request.user in jardin.membres.all():
                            return True
                    # un utilisateur peut commenter une plante sans jardin
                    else:
                        return True

                # pour le test de l'api rest
                else:
                    return True
            # DELETE PUT PATCH
            else:
                return True
        # l'utilisateur non connecté n'a pas de droit de modification
        return False
