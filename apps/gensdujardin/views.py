from django.contrib.auth.models import User
from rest_framework import viewsets
from apps.gensdujardin.models import Profil
from apps.gensdujardin.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer