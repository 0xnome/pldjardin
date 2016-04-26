from rest_framework import viewsets
from apps.gensdujardin.models import Utilisateur
from apps.gensdujardin.serializers import UtilisateurSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer