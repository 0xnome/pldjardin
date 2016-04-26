from rest_framework import serializers
from apps.gensdujardin.models import Utilisateur


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('ville', 'description')