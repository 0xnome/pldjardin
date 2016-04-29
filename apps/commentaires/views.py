from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from apps.commentaires.models import CommentairePlante, CommentaireJardin, CommentaireLopin
from apps.commentaires.serializer import CommentairePlanteSerializer, CommentaireJardinSerializer, \
    CommentaireLopinSerializer
from apps.commentaires.permissions import CommentaireJardinPermission, CommentaireLopinPermission,\
    CommentairePlantePermission
from apps.gensdujardin.serializers import UserFullSerializer
from apps.jardin.serializers import PlanteFullSerializer, JardinFullSerializer, LopinFullSerializer


class CommentairePlanteViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
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
        serializer = PlanteFullSerializer(plante)
        return Response(serializer.data)

class CommentaireJardinViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
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
        serializer = JardinFullSerializer(jardin)
        return Response(serializer.data)


class CommentaireLopinViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
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
        serializer = LopinFullSerializer(lopin)
        return Response(serializer.data)
