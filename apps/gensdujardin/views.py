import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import status, mixins

from apps.actions.serializers import ActionFullSerializer
from apps.gensdujardin.serializers import UserFullSerializer, InscriptionSerializer, UserAuthenticatedSerializer, \
    UserUnauthenticatedSerializer, UserUpdateSerializer

from apps.jardin.serializers import JardinFullSerializer
from rest_framework import viewsets
from apps.gensdujardin.serializers import UserFullSerializer
from apps.gensdujardin.permission import UtilisateurPermission

#class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    permission_classes = (UtilisateurPermission,)
    queryset = User.objects.filter(is_active=True).all()

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return UserUpdateSerializer
        if self.action == "create": # desactivée, la création se fait par /utilisateurs/inscription/
            return InscriptionSerializer
        else:
            if self.request.user and self.request.user.is_authenticated():
                return UserAuthenticatedSerializer
        return UserUnauthenticatedSerializer

    def perform_destroy(self, instance):
        # on désactive l'utilisateur plutot que de le supprimer de la base.
        # TODO: Savoir que faire d'un utilisateur qui quitte le site. Pour l'instant on la desactive, ce qui lui permettra de ne plus etre dans la liste des utilisateurs tout en conservant son profil. Cepandant les objets qui lui sont lié existent toujours et sont visibles. Cela peut poser des problèmes d'anonymat : doit - on changer son nom/prenom/avatar ? Que faire si c'etait la seule admin d'un jardin ?
        instance.is_active = False
        instance.save()

    @list_route(methods=["GET"])
    def moi(self, request, pk=None):
        user = request.user
        if user is not None and user.is_authenticated():
            serializer = UserFullSerializer(user)
            return Response(serializer.data)
        return Response('{"details":"Vous devez être connecté pour acceder à cette ressource"}',
                        status=status.HTTP_403_FORBIDDEN)

    @detail_route(methods=["GET"])
    def membre_jardins(self, request, pk=None):
        user = self.get_object()
        jardins = user.membre_jardins.all()
        serializer = JardinFullSerializer(jardins, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def admin_jardins(self, request, pk=None):
        user = self.get_object()
        jardins = user.admin_jardins.all()
        serializer = JardinFullSerializer(jardins, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def actions(self, request, pk=None):
        user = self.get_object()
        actions = user.actions.all()
        serializer = ActionFullSerializer(actions, many=True)
        return Response(serializer.data)

    @list_route(methods=["POST"])
    def inscription(self, request):
        serializer = InscriptionSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            user = User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = {
                "token": jwt_encode_handler(payload)
            }
            return HttpResponse(json.dumps(token), content_type="application/json", status=status.HTTP_201_CREATED)
        return HttpResponse(JSONRenderer().render(serializer.errors), content_type="application/json", status=status.HTTP_400_BAD_REQUEST)
