from django.contrib.auth.models import User
from rest_framework import serializers
from apps.gensdujardin.models import Utilisateur


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UtilisateurSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Utilisateur
        fields = ('id', 'ville', 'description', 'user')

