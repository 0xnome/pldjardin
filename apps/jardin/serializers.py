from rest_framework import serializers
from apps.jardin.models import Jardin, Adresse

class AdresseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adresse
        fields = ('id', 'ville', 'code_postal', 'rue', 'long', 'lat')

class JardinSerializer(serializers.HyperlinkedModelSerializer):
    adresse = AdresseSerializer(many=False, read_only=True)
    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'horaire', 'image', 'description', 'restreint', 'adresse')