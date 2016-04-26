from rest_framework import serializers
from apps.jardin.models import Jardin, Adresse, Lopin, Actualite, Plante


"""
    Serializers basiques
"""


class AdresseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adresse
        fields = ('id', 'ville', 'code_postal', 'rue', 'long', 'lat')


class JardinSerializer(serializers.HyperlinkedModelSerializer):
    adresse = AdresseSerializer(many=False, read_only=True)

    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'horaire', 'image', 'description', 'restreint', 'adresse')


class LopinSerializer(serializers.HyperlinkedModelSerializer):
    adresse = AdresseSerializer(many=False, read_only=True)

    class Meta:
        model = Lopin
        fields = ('id', 'adresse', 'jardin', 'nom', 'description')


class ActualiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actualite
        fields = ('id', 'jardin', 'texte', 'date_creation')


class PlanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plante
        fields = ('id', 'lopin', 'nom', 'image', 'espece', 'description')
