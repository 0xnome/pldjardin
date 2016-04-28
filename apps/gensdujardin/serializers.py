from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from apps.gensdujardin.models import Profil


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ('id', 'ville', 'presentation', 'avatar', 'user')


class UserSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer(many=False)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'profil')

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
