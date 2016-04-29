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


class ActualitePermission(permissions.BasePermission):
    """
    Global permissions for ActualiteJardin
    """
    def has_object_permission(self, request, view, obj):
        # get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        elif permissions.IsAuthenticated:
            if request.method in ["PATCH","PUT", "DELETE"]:
                # L'utilisateur admin peut modifier,supprimer une actualite
                if request.user in obj.jardin.administrateurs.all():
                    return True
                return False
        return False

    # TODO: empecher un admin d'attribuer son actualite a un autre jardin
    def has_permission(self, request, view):
        # get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        # utilisateur connecté
        elif permissions.IsAuthenticated.has_permission(self,request,view):
            if request.method == "POST":
                if "jardin" in request.data:
                    id = int(request.data["jardin"])
                    # Un admin seulement peut crée une actualite sur son jardin
                    if request.user in Jardin.objects.get(pk=id).administrateurs.all():
                        return True
                # necessaire pour le test de l'api
                elif not ("jardin" in request.data):
                    return True
            else:
                return True
        return False
