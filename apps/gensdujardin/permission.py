from rest_framework import permissions



class UtilisateurPermission(permissions.IsAuthenticatedOrReadOnly):
    """
    Permission pour les utilisateurs
    """

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE" or request.method == "PUT" or request.method == "PATCH":
            return request.user == obj
        return True
