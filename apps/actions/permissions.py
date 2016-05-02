from rest_framework import permissions

from apps.jardin.models import Plante


class ActionPermission(permissions.IsAuthenticatedOrReadOnly):
    """
    Definit les permissions pour les actions
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # get, Head, Option
            return True
        # POST, DELETE si utilisateur
        return request.user == obj.utilisateur or \
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