import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import status

from apps.actions.serializers import ActionSerializer
from apps.gensdujardin.serializers import UserSerializer, InscriptionSerializer

from apps.jardin.serializers import JardinSerializer
from rest_framework import viewsets
from apps.gensdujardin.serializers import UserSerializer
from apps.gensdujardin.permission import UtilisateurPermission

class UserViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """

    permission_classes = (UtilisateurPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=["GET"])
    def moi(self, request, pk=None):
        user = request.user
        if user.is_authenticated():
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response("Vous devez être connecté pour acceder à cette ressource",
                        status=status.HTTP_403_FORBIDDEN)

    @detail_route(methods=["GET"])
    def membre_jardins(self, request, pk=None):
        user = self.get_object()
        jardins = user.membre_jardins.all()
        serializer = JardinSerializer(jardins, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def admin_jardins(self, request, pk=None):
        user = self.get_object()
        jardins = user.admin_jardins.all()
        serializer = JardinSerializer(jardins, many=True)
        return Response(serializer.data)

    @detail_route(methods=["GET"])
    def actions(self, request, pk=None):
        user = self.get_object()
        actions = user.actions.all()
        serializer = ActionSerializer(actions, many=True)
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
            return HttpResponse(json.dumps(token), content_type="application/json", status=201)

        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
