from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from apps.gensdujardin.models import Profil
from apps.jardin.serializers import JardinFullSerializer


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ('id', 'ville', 'presentation', 'avatar')


class UserFullSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer()

    class Meta:
        model = User
        fields = ('id', 'profil', 'last_login', 'username', 'first_name', 'last_name', 'email', 'date_joined' )


class UserUpdateSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer()

    class Meta:
        model = User
        fields = ('id', 'profil', 'first_name', 'last_name', 'email')

    def update(self, instance, validated_data):
        profil = instance.profil
        profil_data = {}
        if "profil" in validated_data:
            profil_data = validated_data.pop('profil')

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profil.ville = profil_data.get('ville',profil.ville)
        profil.presentation = profil_data.get('presentation',profil.presentation)
        profil.avatar = profil_data.get('avatar',profil.avatar)
        profil.save()

        return instance


class UserUnauthenticatedSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer()

    class Meta:
        model = User
        fields = ('id', 'profil', 'username')

class UserAuthenticatedSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer()

    class Meta:
        model = User
        fields = ('id', 'profil', 'username', 'first_name', 'last_name')


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

