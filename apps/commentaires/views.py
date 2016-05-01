from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from apps.commentaires.models import CommentairePlante, CommentaireJardin, CommentaireLopin
from apps.commentaires.serializer import CommentairePlanteFullSerializer, CommentaireJardinFullSerializer, \
    CommentaireLopinFullSerializer, CommentaireJardinCreateSerializer, CommentairePlanteCreateSerializer, \
    CommentaireLopinCreateSerializer
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

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(auteur=current_user)

    def get_serializer_class(self):
        if self.action == "create":
            return CommentairePlanteCreateSerializer
        else:
            return CommentairePlanteFullSerializer

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

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(auteur=current_user)

    def get_serializer_class(self):
        if self.action == "create":
            return CommentaireJardinCreateSerializer
        else:
            return CommentaireJardinFullSerializer

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

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(auteur=current_user)

    def get_serializer_class(self):
        if self.action == "create":
            return CommentaireLopinCreateSerializer
        else:
            return CommentaireLopinFullSerializer

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
