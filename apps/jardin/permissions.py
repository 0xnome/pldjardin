from rest_framework import permissions

from apps.jardin.models import Jardin, Lopin, Actualite


class JardinPermission(permissions.IsAuthenticatedOrReadOnly):
    """
    Global permissions for jardins
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user in obj.administrateurs.all()


class LopinPermission(permissions.IsAuthenticatedOrReadOnly):
    """
    Global permissions for lopins
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # get, Head, Option
            return True
        # On peut tout faire sur un lopin public ou il faut etre admin du jardin du lopin
        # TODO: un utilisateur peut il vraiment tout modifiez dans un lopin public ? delete etc...
        return obj.jardin is None or request.user in obj.jardin.administrateurs.all()

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated()):
            if (request.method == "POST"
                and "jardin" in request.data
                and (request.data["jardin"] != "" and request.data["jardin"] is not None)):
                try:
                    jardin = Jardin.objects.get(pk=int(request.data["jardin"]))
                    return request.user in jardin.administrateurs.all()
                except:
                    return False
            # DELETE PUT PATCH et jardin vide
            else:
                return True
        else:
            return False


class PlantePermission(permissions.IsAuthenticatedOrReadOnly):
    """
    Global permissions for plantes
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # get, Head, Option
            return True
        if obj.lopin.jardin is not None:
            if not obj.lopin.jardin.restreint:
                # si le jardin n'est pas restreint
                return True
            elif request.user in obj.lopin.jardin.membres.all():
                # il faut etre membre du jardin du lopin pour le modifier
                return True
            else:
                return False
        else:
            # On peut tout faire sur un plante d'un lopin public
            return True

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated()):
            if (request.method == "POST" and "lopin" in request.data):
                try:
                    lopin = Lopin.objects.get(pk=int(request.data["lopin"]))
                    return (lopin.jardin is None
                            or not lopin.jardin.restreint
                            or request.user in lopin.jardin.membres.all())
                except:
                    return False
            # DELETE PUT PATCH
            else:
                return True
        else:
            return False


class ActualitePermission(permissions.IsAuthenticatedOrReadOnly):
    """
    Global permissions for Actualite
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # get, Head, Option
            return True
        # POST, DELETE si admin
        return request.user in obj.jardin.administrateurs.all()

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated()):
            if (request.method == "POST" and "jardin" in request.data):
                try:
                    jardin = Jardin.objects.get(pk=int(request.data["jardin"]))
                    return request.user in jardin.administrateurs.all()
                except:
                    return False
            elif request.method == "DELETE":
                return True
            else:
                return True
        else:
            return False

class AdressePermission(permissions.IsAuthenticatedOrReadOnly):
    """
    Global permissions for ActualiteJardin
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # get, Head, Option
            return True
        # On peut modifier l'adresse d'un lopin public ou il faut etre admin du jardin du lopin
        if obj.jardins.count():
            for jardin in obj.jardins.all():
                if request.user in jardin.administrateurs.all():
                    return True
            return False
        return True
