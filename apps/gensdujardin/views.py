from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from apps.gensdujardin.models import Profil
from apps.gensdujardin.serializers import UserSerializer, UserAvecMembreJardinsSerializer
from apps.jardin.serializers import JardinSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

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




