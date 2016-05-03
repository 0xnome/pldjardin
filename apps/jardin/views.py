from django.db.models import Q
from django.http import HttpResponse

from rest_framework import viewsets, mixins, status
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from apps.actions.serializers import ActionFullSerializer
from apps.commentaires.serializer import CommentaireJardinFullSerializer, CommentaireLopinFullSerializer, \
    CommentairePlanteFullSerializer
from apps.gensdujardin.serializers import UserFullSerializer
from apps.jardin.models import Jardin, Adresse, Lopin, Actualite, Plante
from apps.jardin.serializers import JardinFullSerializer, AdresseFullSerializer, LopinFullSerializer, \
    ActualiteFullSerializer, \
    PlanteFullSerializer, JardinCreateSerializer, JardinUpdateSerializer, LopinUpdateSerializer, PlanteUpdateSerializer, \
    AdresseUpdateSerializer, ResultsSerializer, AdresseCreateSerializer, LopinCreateSerializer, \
    ActualiteCreateSerializer
from apps.jardin.permissions import JardinPermission, LopinPermission, PlantePermission, ActualitePermission, \
    AdressePermission


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

    def perform_destroy(self, instance):
        adresse = instance.adresse
        instance.delete()
        adresse.delete()

    @detail_route(methods=["GET"])
    def commentaires(self, request, pk=None):
        jardin = self.get_object()
        commentaires = jardin.commentaires.all()
        serializer = CommentaireJardinFullSerializer(commentaires, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def actualites(self, request, pk=None):
        jardin = self.get_object()
        actualites = jardin.actualites.all()
        serializer = ActualiteFullSerializer(actualites, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def membres(self, request, pk=None):
        jardin = self.get_object()
        membres = jardin.membres.all()
        serializer = UserFullSerializer(membres, many=True)
        data = serializer.data
        for user in data:
            image = user["profil"]["avatar"]
            if image and "http://" not in image:
                # si l'http n'est pas dans l'image
                user["profil"]["avatar"] = self.request.build_absolute_uri('/') + image[1:]
        return Response(data)

    @detail_route(methods=["GET"])
    def administrateurs(self, request, pk=None):
        jardin = self.get_object()
        administrateurs = jardin.administrateurs.all()
        serializer = UserFullSerializer(administrateurs, many=True)
        data = serializer.data
        for user in data:
            image = user["profil"]["avatar"]
            if image and "http://" not in image:
                # si l'http n'est pas dans l'image
                user["profil"]["avatar"] = self.request.build_absolute_uri('/') + image[1:]
        return Response(data)

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

    @detail_route(methods=["GET"])
    def rejoindre(self, request, pk=None):
        jardin = self.get_object()
        if request.user and request.user.is_authenticated():
            if request.user not in jardin.membres.all():
                if not jardin.restreint:
                    jardin.membres.add(request.user)
                    jardin.save()
                    return HttpResponse(content=JSONRenderer().render({'message': 'Vous avez rejoind le jardin.'}),
                                        content_type="application/json", status=status.HTTP_200_OK)
                else:
                    return HttpResponse(
                        content=JSONRenderer().render({'error': 'Vous ne pouvez pas rejoindre un jardin restreint !'}),
                        content_type="application/json", status=status.HTTP_403_FORBIDDEN)
            else:
                return HttpResponse(
                    content=JSONRenderer().render({'error': 'Vous aviez déjà rejoind ce jardin !'}),
                    content_type="application/json", status=status.HTTP_403_FORBIDDEN)
        else:
            return HttpResponse(
                content=JSONRenderer().render({'error': 'Vous devez être connecté pour effectuer cette action !'}),
                content_type="application/json", status=status.HTTP_403_FORBIDDEN)

    @detail_route(methods=["GET"])
    def quitter(self, request, pk=None):
        user = request.user
        jardin = self.get_object()
        if user and user.is_authenticated():
            if user in jardin.membres.all():
                if user in jardin.administrateurs.all():
                    if jardin.administrateurs.count() > 1:
                        jardin.administrateurs.remove(user)
                    else:
                        return HttpResponse(
                            content=JSONRenderer().render(
                                {'error': 'Vous etes le dernier admin du jardin, vous ne pouvez pas le quitter !'}),
                            content_type="application/json", status=status.HTTP_403_FORBIDDEN)
                jardin.membres.remove(user)
                jardin.save()
                return HttpResponse(content=JSONRenderer().render({'message': 'Vous avez quitté le jardin.'}),
                                    content_type="application/json", status=status.HTTP_200_OK)
            else:
                return HttpResponse(
                    content=JSONRenderer().render({'error': 'Vous n\etes pas membres de jardin !'}),
                    content_type="application/json", status=status.HTTP_403_FORBIDDEN)
        else:
            return HttpResponse(
                content=JSONRenderer().render({'error': 'Vous devez être connecté pour effectuer cette action !'}),
                content_type="application/json", status=status.HTTP_403_FORBIDDEN)


class AdresseViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    permission_classes = (AdressePermission,)
    queryset = Adresse.objects.all()

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
        data = serializer.data
        for jardin in data:
            image = jardin["image"]
            if image and "http://" not in image:
                # si l'http n'est pas dans l'image
                jardin["image"] = self.request.build_absolute_uri('/') + image[1:]
        return Response(data)

    @detail_route(methods=["GET"])
    def lopins(self, request, pk=None):
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
        elif self.action == "create":
            return LopinCreateSerializer
        else:
            return LopinFullSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        adresse = instance.adresse
        jardin = instance.jardin
        instance.delete()
        # On supprime l'adresse d'un lopin indépendant
        if jardin is None:
            adresse.delete()

    @detail_route(methods=["GET"])
    def commentaires(self, request, pk=None):
        lopin = self.get_object()
        commentaires = lopin.commentaires.all()
        serializer = CommentaireLopinFullSerializer(commentaires, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def actions(self, request, pk=None):
        lopin = self.get_object()
        actions = []
        for plante in lopin.plantes.all():
            actions = actions + list(plante.actions.all())
        serializer = ActionFullSerializer(actions, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def plantes(self, request, pk=None):
        lopin = self.get_object()
        plantes = lopin.plantes.all()
        serializer = PlanteFullSerializer(plantes, many=True)
        data = serializer.data
        for plante in data:
            image = plante["image"]
            if image and "http://" not in image:
                # si l'http n'est pas dans l'image
                plante["image"] = self.request.build_absolute_uri('/') + image[1:]
        return Response(data)

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
        data = serializer.data
        image = data["image"]
        if image and "http://" not in image:
            # si l'http n'est pas dans l'image
            data["image"] = self.request.build_absolute_uri('/') + image[1:]
        return Response(data)


class ActualiteViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    permission_classes = (ActualitePermission,)
    queryset = Actualite.objects.all()

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(auteur=current_user)

    def get_serializer_class(self):
        if self.action == "create":
            return ActualiteCreateSerializer
        else:
            return ActualiteFullSerializer

    @detail_route(methods=["GET"])
    def jardin(self, request, pk=None):
        actualite = self.get_object()
        jardin = actualite.jardin
        serializer = JardinFullSerializer(jardin)
        data = serializer.data
        image = data["image"]
        if image and "http://" not in image:
            # si l'http n'est pas dans l'image
            data["image"] = self.request.build_absolute_uri('/') + image[1:]
        return Response(data)

    @detail_route(methods=["GET"])
    def auteur(self, request, pk=None):
        actualite = self.get_object()
        auteur = actualite.auteur
        serializer = UserFullSerializer(auteur)
        data = serializer.data
        image = data["profil"]["avatar"]
        if image and "http://" not in image:
            # si l'http n'est pas dans l'image
            data["profil"]["avatar"] = self.request.build_absolute_uri('/') + image[1:]
        return Response(data)


class PlanteViewSet(viewsets.ModelViewSet):
    permission_classes = (PlantePermission,)
    queryset = Plante.objects.all()

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return PlanteUpdateSerializer
        else:
            return PlanteFullSerializer

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(utilisateur=current_user)

    @detail_route(methods=["GET"])
    def commentaires(self, request, pk=None):
        plante = self.get_object()
        commentaires = plante.commentaires.all()
        serializer = CommentairePlanteFullSerializer(commentaires, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def actions(self, request, pk=None):
        plante = self.get_object()
        actions = plante.actions.all()
        serializer = ActionFullSerializer(actions, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def lopin(self, request, pk=None):
        plante = self.get_object()
        lopin = plante.lopin
        serializer = LopinFullSerializer(lopin)
        return Response(serializer.data)


def recherche(request):
    keywords = ""
    if "q" in request.GET and request.GET["q"] != "":
        keywords = request.GET["q"]

    keywordlist = keywords.split()

    class Results(object):
        def __init__(self, jardins=None, lopins=None, plantes=None, adresses=None):
            self.jardins = jardins
            self.lopins = lopins
            self.plantes = plantes
            self.adresses = adresses

    filterjardins = lambda keyword: (
        Q(nom__icontains=keyword) | Q(description__icontains=keyword) | Q(adresse__ville__icontains=keyword) |
        Q(adresse__rue__icontains=keyword) | Q(adresse__code_postal__icontains=keyword) |
        Q(lopins__plantes__nom__icontains=keyword) | Q(lopins__plantes__espece__icontains=keyword)
    )
    filterlopins = lambda keyword: (
        Q(nom__icontains=keyword) | Q(description__icontains=keyword) | Q(
        adresse__ville__icontains=keyword) | Q(adresse__rue__icontains=keyword) | Q(
        adresse__code_postal__icontains=keyword)  | Q(plantes__nom__icontains=keyword) |
        Q(plantes__espece__icontains=keyword)
    )
    filterplantes = lambda keyword: (
        Q(nom__icontains=keyword) | Q(description__icontains=keyword) | Q(espece__icontains=keyword) | Q(
            lopin__adresse__ville__icontains=keyword) | Q(lopin__adresse__rue__icontains=keyword) | Q(
            lopin__adresse__code_postal__icontains=keyword)
    )
    filteradresses = lambda keyword: (
        Q(ville__icontains=keyword) | Q(rue__icontains=keyword) | Q(code_postal__icontains=keyword)
    )

    jardins_query = Jardin.objects
    lopins_query = Lopin.objects
    plantes_query = Plante.objects
    # adresses_query = Adresse.objects

    for keyword in keywordlist:
        jardins_query = jardins_query.filter(filterjardins(keyword))
        lopins_query = lopins_query.filter(filterlopins(keyword))
        plantes_query = plantes_query.filter(filterplantes(keyword))
        # adresses_query = adresses_query.filter(filteradresses(keyword))

    results = Results(jardins=jardins_query,
                      lopins=lopins_query,
                      plantes=plantes_query,
                      # adresses=adresses_query
                      )

    serializer = ResultsSerializer(results)
    return HttpResponse(content=JSONRenderer().render(serializer.data), content_type="application/json",
                        status=status.HTTP_200_OK)
