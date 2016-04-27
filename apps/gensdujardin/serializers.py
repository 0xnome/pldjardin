from django.contrib.auth.models import User
from rest_framework import serializers
from apps.gensdujardin.models import Profil


class ProfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profil
        fields = ('id', 'ville', 'description', 'avatar' )

class UserSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'profil')


