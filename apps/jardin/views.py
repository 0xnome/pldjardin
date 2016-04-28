from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from apps.actions.serializers import ActionSerializer
from apps.commentaires.serializer import CommentaireJardinSerializer, CommentaireLopinSerializer, \
    CommentairePlanteSerializer
from apps.gensdujardin.serializers import UserFullSerializer
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
        serializer = UserFullSerializer(membres, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def administrateurs(self, request, pk=None):
        jardin = self.get_object()
        administrateurs = jardin.administrateurs.all()
        serializer = UserFullSerializer(administrateurs, many=True)
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

    @detail_route(methods=["GET"])
    def jardins(self, request, pk=None):
        adresse = self.get_object()
        jardins = adresse.jardins.all()
        serializer = JardinSerializer(jardins, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def lopins(self, request, pk=None):
        # TODO union avec les lopins du jardin a cette adresse ?
        adresse = self.get_object()
        lopins = adresse.lopins.all()
        serializer = LopinSerializer(lopins, many=True)
        return Response(serializer.data)


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
    def plantes(self, request, pk=None):
        lopin = self.get_object()
        plantes = lopin.plantes.all()
        serializer = PlanteSerializer(plantes, many=True)
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

    @detail_route(methods=["GET"])
    def jardin(self, request, pk=None):
        actualite = self.get_object()
        jardin = actualite.jardin
        serializer = JardinSerializer(jardin)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def auteur(self, request, pk=None):
        actualite = self.get_object()
        auteur = actualite.auteur
        serializer = UserFullSerializer(auteur)
        return Response(serializer.data)

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

    @detail_route(methods=["GET"])
    def actions(self, request, pk=None):
        plante = self.get_object()
        actions = plante.actions.all()
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def lopin(self, request, pk=None):
        plante = self.get_object()
        lopin = plante.lopin
        serializer = LopinSerializer(lopin)
        return Response(serializer.data)