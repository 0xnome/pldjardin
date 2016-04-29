from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from apps.actions.serializers import ActionSerializer
from apps.commentaires.serializer import CommentaireJardinSerializer, CommentaireLopinSerializer, \
    CommentairePlanteSerializer
from apps.gensdujardin.serializers import UserFullSerializer
from apps.jardin.models import Jardin, Adresse, Lopin, Actualite, Plante
from apps.jardin.serializers import JardinFullSerializer, AdresseFullSerializer, LopinFullSerializer, ActualiteSerializer, \
    PlanteFullSerializer, JardinCreateSerializer, JardinUpdateSerializer, LopinUpdateSerializer, PlanteUpdateSerializer, \
    AdresseUpdateSerializer, ResultsSerializer
from apps.jardin.permissions import JardinPermission, LopinPermission, PlantePermission, ActualitePermission

class JardinViewSet(viewsets.ModelViewSet):
    permission_classes = (JardinPermission,)
    queryset = Jardin.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return JardinFullSerializer
        elif self.action == "create":
            return JardinCreateSerializer
        else:
            return JardinUpdateSerializer

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(administrateurs=[current_user], membres=[current_user])


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
    def lopins(self, request, pk=None):
        jardin = self.get_object()
        lopins = jardin.lopins.all()
        serializer = LopinFullSerializer(lopins, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def adresse(self, request, pk=None):
        jardin = self.get_object()
        adresse = jardin.adresse
        serializer = AdresseFullSerializer(adresse)
        return Response(serializer.data)


class AdresseViewSet(viewsets.ModelViewSet):
    queryset = Adresse.objects.all()
    serializer_class = AdresseFullSerializer

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return AdresseUpdateSerializer
        else:
            return AdresseFullSerializer

    @detail_route(methods=["GET"])
    def jardins(self, request, pk=None):
        adresse = self.get_object()
        jardins = adresse.jardins.all()
        serializer = JardinFullSerializer(jardins, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def lopins(self, request, pk=None):
        # TODO union avec les lopins du jardin a cette adresse ?
        adresse = self.get_object()
        lopins = adresse.lopins.all()
        serializer = LopinFullSerializer(lopins, many=True)
        return Response(serializer.data)


class LopinViewSet(viewsets.ModelViewSet):
    permission_classes = (LopinPermission,)
    queryset = Lopin.objects.all()

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return LopinUpdateSerializer
        else:
            return LopinFullSerializer

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
        serializer = PlanteFullSerializer(plantes, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def adresse(self, request, pk=None):
        lopin = self.get_object()
        adresse = lopin.adresse
        serializer = AdresseFullSerializer(adresse)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def jardin(self, request, pk=None):
        lopin = self.get_object()
        jardin = lopin.jardin
        serializer = JardinFullSerializer(jardin)
        return Response(serializer.data)


class ActualiteViewSet(viewsets.ModelViewSet):
    permission_classes = (ActualitePermission,)
    queryset = Actualite.objects.all()
    serializer_class = ActualiteSerializer

    @detail_route(methods=["GET"])
    def jardin(self, request, pk=None):
        actualite = self.get_object()
        jardin = actualite.jardin
        serializer = JardinFullSerializer(jardin)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def auteur(self, request, pk=None):
        actualite = self.get_object()
        auteur = actualite.auteur
        serializer = UserFullSerializer(auteur)
        return Response(serializer.data)

class PlanteViewSet(viewsets.ModelViewSet):
    permission_classes = (PlantePermission,)
    queryset = Plante.objects.all()

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return PlanteUpdateSerializer
        else:
            return PlanteFullSerializer

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
        serializer = LopinFullSerializer(lopin)
        return Response(serializer.data)


def recherche(request):
    print(request.GET)

    class Results(object):
        def __init__(self, jardins=None, lopins=None, plantes=None, adresses=None):
            self.jardins = jardins
            self.lopins = lopins
            self.plantes = plantes
            self.adresses = adresses

    results = Results(jardins=Jardin.objects.all(),
                      lopins=Lopin.objects.all(),
                      plantes=Plante.objects.all(),
                      adresses=Adresse.objects.all())
    serializer = ResultsSerializer(results)
    return HttpResponse(content=JSONRenderer().render(serializer.data))