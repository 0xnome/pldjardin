from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from apps.gensdujardin.models import Profil
from apps.jardin.serializers import JardinSerializer


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ('id', 'ville', 'presentation', 'avatar', 'user')


class UserSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'profil')


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

