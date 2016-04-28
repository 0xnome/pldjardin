from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from apps.actions.serializers import ActionSerializer
from apps.commentaires.serializer import CommentaireJardinSerializer, CommentaireLopinSerializer, \
    CommentairePlanteSerializer
from apps.gensdujardin.serializers import UserSerializer
from apps.jardin import permissions
from apps.jardin.models import Jardin, Adresse, Lopin, Actualite, Plante
from apps.jardin.serializers import JardinSerializer, AdresseSerializer, LopinSerializer, ActualiteSerializer, \
    PlanteSerializer
from apps.jardin.permissions import JardinPermission, LopinPermission, PlantePermission, ActualitePermission


class JardinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """

    permission_classes = (JardinPermission,)
    queryset = Jardin.objects.all()
    serializer_class = JardinSerializer

    @detail_route(methods=["GET"])
    def commentaires(self, request, pk=None):
        jardin = self.get_object()
        commentaires = jardin.commentaires.all()
        serializer = CommentaireJardinSerializer(commentaires, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def actualites(self, request, pk=None):
        jardin = self.get_object()
        actualites = jardin.actualites.all()
        serializer = ActualiteSerializer(actualites, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def membres(self, request, pk=None):
        jardin = self.get_object()
        membres = jardin.membres.all()
        serializer = UserSerializer(membres, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def administrateurs(self, request, pk=None):
        jardin = self.get_object()
        administrateurs = jardin.administrateurs.all()
        serializer = UserSerializer(administrateurs, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def adresse(self, request, pk=None):
        jardin = self.get_object()
        adresse = jardin.adresse
        serializer = AdresseSerializer(adresse)
        return Response(serializer.data)


class AdresseViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """

    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer


class LopinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """

    permission_classes = (LopinPermission,)
    queryset = Lopin.objects.all()
    serializer_class = LopinSerializer

    @detail_route(methods=["GET"])
    def commentaires(self, request, pk=None):
        lopin = self.get_object()
        commentaires = lopin.commentaires.all()
        serializer = CommentaireLopinSerializer(commentaires, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def actions(self, request, pk=None):
        lopin = self.get_object()
        actions = lopin.actions.all()
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def adresse(self, request, pk=None):
        lopin = self.get_object()
        adresse = lopin.adresse
        serializer = AdresseSerializer(adresse)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def jardin(self, request, pk=None):
        lopin = self.get_object()
        jardin = lopin.jardin
        serializer = JardinSerializer(jardin)
        return Response(serializer.data)


class ActualiteViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    permission_classes = (ActualitePermission,)
    queryset = Actualite.objects.all()
    serializer_class = ActualiteSerializer


class PlanteViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """

    permission_classes = (PlantePermission,)
    queryset = Plante.objects.all()
    serializer_class = PlanteSerializer

    @detail_route(methods=["GET"])
    def commentaires(self, request, pk=None):
        plante = self.get_object()
        commentaires = plante.commentaires.all()
        serializer = CommentairePlanteSerializer(commentaires, many=True)
        return Response(serializer.data)
