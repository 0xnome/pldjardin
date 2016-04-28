from rest_framework import permissions



class UtilisateurPermission(permissions.BasePermission):
    """
    Permission pour les utilisateurs
    """


    def has_permission(self, request, view):
        if permissions.IsAuthenticated.has_permission(self,request,view):
            # un utlisateur ne peut pas en cree si il est deja connecté
            if request.method == "POST":
                return False
            elif request.method in ["GET","PUT", "PATCH", "DELETE, OPTION, HEAD"]:
                return True
            # il est interdit de supprimer un utilisateur
            elif request.method in [ "DELETE"]:
                return False

        elif request.method in ["POST","GET"]:
            return True
        return False


    def has_object_permission(self, request, view, obj):

        if request.method == "GET":
            # TODO: ------------ changer ici le comportement!!
            return True
        elif request.method == "POST":
            return True
        # DELETE PUT PATCH
        elif permissions.IsAuthenticated.has_permission(self, request, view):
            if request.method == "DELETE":
                return False
            elif request.method in ["PUT","PATCH"]:
                if obj == request.user:
                    return True
        return False
