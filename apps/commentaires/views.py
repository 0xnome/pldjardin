from rest_framework import viewsets

from apps.commentaires.models import CommentairePlante, CommentaireJardin, CommentaireLopin, Commentaire
from apps.commentaires.serializer import CommentairePlanteSerializer, CommentaireJardinSerializer, \
    CommentaireLopinSerializer
from apps.commentaires.permissions import CommentaireJardinPermission, CommentaireLopinPermission

class CommentairePlanteViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = CommentairePlante.objects.all()
    serializer_class = CommentairePlanteSerializer


class CommentaireJardinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    permission_classes = (CommentaireJardinPermission,)
    queryset = CommentaireJardin.objects.all()
    serializer_class = CommentaireJardinSerializer


class CommentaireLopinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    permission_classes = (CommentaireLopinPermission,)
    queryset = CommentaireLopin.objects.all()
    serializer_class = CommentaireLopinSerializer
