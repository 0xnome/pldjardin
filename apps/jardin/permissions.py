from rest_framework import permissions

from apps.jardin.models import Jardin, Lopin, Actualite


class JardinPermission(permissions.BasePermission):
    """
    Global permissions for jardins
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        elif permissions.IsAuthenticated.has_permission(self,request,view):
            return request.user in obj.administrateurs.all()
        return False

    def has_permission(self, request, view):
        # get option head
        if request.method in permissions.SAFE_METHODS:
            return True
        # un utilisateur ne peut cree un jardin que si il est connecté
        if request.method == "POST":
            if permissions.IsAuthenticated.has_permission(self,request,view):
                return True
            else:
                return False
        # path put delete
        return True

class LopinPermission(permissions.BasePermission):
    """
    Global permissions for lopins
    """

    def has_object_permission(self, request, view, obj):

        # get, Head, Option
        if request.method in permissions.SAFE_METHODS:
            return True

        #  Post, Patch, Put, Delete
        else:
            if obj.jardin:
                if request.user in obj.jardin.administrateurs.all():
                    return True

                # TODO: un utilisateur peut il vraiment tout modifiez dans un lopin public ? delete etc...
                else:
                    return False

        return True

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        elif permissions.IsAuthenticated.has_permission(self,request,view):
            if request.method == "POST":
                if "jardin" in request.data:
                    id = request.data["jardin"]

                    # tout le monde peut créer un lopin sans jardin
                    if id == "":
                        return True
                    # Un admin seulement peut créer un lopin sur son jardin
                    else:
                        return request.user in Jardin.objects.get(pk=int(id)).administrateurs.all()

                # necessaire pour tester l'api + creation de lopin hors jardin
                else:
                    return True
            #  DELETE PUT PATCH
            else:
                return True
        else:
            return False




        if "jardin" in request.data:
            id = request.data["jardin"]
            if id:
                if not (request.user in Jardin.objects.get(pk=int(id)).administrateurs.all()):
                    return False
        return True
        # TODO: un utilisateur peut il vraiment tout modifiez dans un lopin public ? delete etc...




class PlantePermission(permissions.BasePermission):
    """
    Global permissions for plantes
    """

    def has_object_permission(self, request, view, obj):
        # GET HEAD OPTION
        if request.method in permissions.SAFE_METHODS:
            if obj.lopin.jardin:
                if request.user in obj.lopin.jardin.membres.all():
                    return True
                elif obj.lopin.jardin.restreint:
                    return False
            else:
                return True
        # PUT PATCH POST DELETE
        else:
            if obj.lopin.jardin:
                if request.user in obj.lopin.jardin.membres.all():
                    return True
                else:
                    return False
            else:
                # TODO: un utilisateur peut il vraiment tout modifiez dans ue plante public ? delete etc...
                return True

    def has_permission(self, request, view):
        # GET OPTION HEAD
        if request.method in permissions.SAFE_METHODS:
            return True
        # POST PATCH PUT DELETE
        if "lopin" in request.data:
            lopin = Lopin.objects.get(pk = int(request.data["lopin"]))
            if lopin.jardin:
                if not (request.user in lopin.jardin.membres.all()):
                    return False
            return True
        else:
            return True
            # TODO: un utilisateur peut il vraiment tout modifiez dans un lopin public ? delete etc...



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
                    if request.user in Jardin.objects.get(pk=id).membres.all():
                        return True
                # necessaire pour le test de l'api
                elif not ("jardin" in request.data):
                    return True
            else:
                return True
        return False
