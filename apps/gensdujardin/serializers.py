from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from apps.gensdujardin.models import Profil
from apps.jardin.serializers import JardinSerializer


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ('id', 'ville', 'presentation', 'avatar', 'user')


class UserFullSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer()

    class Meta:
        model = User
        fields = ('id', 'profil', 'last_login', 'username', 'first_name', 'last_name', 'email', 'date_joined' )


class UserUnauthenticatedSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer()

    class Meta:
        model = User
        fields = ('id', 'profil', 'username', 'first_name', 'last_name')

class UserAuthenticatedSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer()

    class Meta:
        model = User
        fields = ('id', 'profil', 'username', 'first_name', 'last_name')


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

