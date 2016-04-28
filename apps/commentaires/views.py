from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from apps.commentaires.models import CommentairePlante, CommentaireJardin, CommentaireLopin, Commentaire
from apps.commentaires.serializer import CommentairePlanteSerializer, CommentaireJardinSerializer, \
    CommentaireLopinSerializer
from apps.commentaires.permissions import CommentaireJardinPermission, CommentaireLopinPermission,\
    CommentairePlantePermission
from apps.gensdujardin.serializers import UserFullSerializer
from apps.jardin.serializers import PlanteSerializer, JardinSerializer, LopinSerializer


class CommentairePlanteViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    permission_classes = (CommentairePlantePermission,)
    queryset = CommentairePlante.objects.all()
    serializer_class = CommentairePlanteSerializer

    @detail_route(methods=["GET"])
    def auteur(self, request, pk=None):
        commentaire = self.get_object()
        adresse = commentaire.adresse
        serializer = UserFullSerializer(adresse)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def plante(self, request, pk=None):
        commentaire = self.get_object()
        plante = commentaire.plante
        serializer = PlanteSerializer(plante)
        return Response(serializer.data)

class CommentaireJardinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    permission_classes = (CommentaireJardinPermission,)
    queryset = CommentaireJardin.objects.all()
    serializer_class = CommentaireJardinSerializer

    @detail_route(methods=["GET"])
    def auteur(self, request, pk=None):
        commentaire = self.get_object()
        adresse = commentaire.adresse
        serializer = UserFullSerializer(adresse)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def jardin(self, request, pk=None):
        commentaire = self.get_object()
        jardin = commentaire.jardin
        serializer = JardinSerializer(jardin)
        return Response(serializer.data)


class CommentaireLopinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    permission_classes = (CommentaireLopinPermission,)
    queryset = CommentaireLopin.objects.all()
    serializer_class = CommentaireLopinSerializer

    @detail_route(methods=["GET"])
    def auteur(self, request, pk=None):
        commentaire = self.get_object()
        adresse = commentaire.adresse
        serializer = UserFullSerializer(adresse)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def lopin(self, request, pk=None):
        commentaire = self.get_object()
        lopin = commentaire.lopin
        serializer = LopinSerializer(lopin)
        return Response(serializer.data)
