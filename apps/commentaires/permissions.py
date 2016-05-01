from rest_framework import permissions

from apps.jardin.models import Jardin, Lopin, Plante

class CommentairePermission(permissions.IsAuthenticatedOrReadOnly):
    class Meta:
        abstract = True


class CommentaireJardinPermission(CommentairePermission):
    """
    Global permissions for CommentaireJardin
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # get, Head, Option
            return True
        # POST, DELETE si auteur
        return request.user == obj.auteur or request.user in obj.jardin.administrateurs.all()

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated()):
            if (request.method == "POST" and "jardin" in request.data):
                try:
                    jardin = Jardin.objects.get(pk=int(request.data["jardin"]))
                    return not jardin.restreint or request.user in jardin.membres.all()
                except:
                    return False
            elif request.method == "DELETE":
                return True
            else:
                return True
        else:
            return False


class CommentaireLopinPermission(CommentairePermission):
    """
       Global permissions for CommentaireLopin
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # get, Head, Option
            return True
        # POST, DELETE si auteur
        return request.user == obj.auteur or\
               (obj.lopin.jardin is not None and request.user in obj.lopin.jardin.administrateurs.all())

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated()):
            if (request.method == "POST" and "lopin" in request.data):
                try:
                    lopin = Lopin.objects.get(pk=int(request.data["lopin"]))
                    return lopin.jardin is None or not lopin.jardin.restreint or request.user in lopin.jardin.membres.all()
                except:
                    return False
            elif request.method == "DELETE":
                return True
            else:
                return True
        else:
            return False


class CommentairePlantePermission(CommentairePermission):
    """
       Global permissions for CommentairePlante
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # get, Head, Option
            return True
        # POST, DELETE si auteur
        return request.user == obj.auteur or\
               (obj.plante.lopin.jardin is not None and request.user in obj.plante.lopin.jardin.administrateurs.all())

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated()):
            if (request.method == "POST" and "plante" in request.data):
                try:
                    plante = Plante.objects.get(pk=int(request.data["plante"]))
                    return plante.lopin.jardin is None or not plante.lopin.jardin.restreint or request.user in plante.lopin.jardin.membres.all()
                except:
                    return False
            elif request.method == "DELETE":
                return True
            else:
                return True
        else:
            return False
