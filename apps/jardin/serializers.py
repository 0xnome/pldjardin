from rest_framework import serializers

from apps.jardin.models import Jardin, Adresse, Lopin, Actualite, Plante


"""
    Serializers basiques
"""


class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = ('id', 'ville', 'code_postal', 'rue', 'long', 'lat')


class JardinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'actualites', 'lopins', 'commentaires', 'site', 'contact', 'horaire', 'image', 'description', 'restreint', 'compostier', 'adresse', 'administrateurs', 'membres')


class LopinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lopin
        fields = ('id', 'adresse', 'jardin', 'nom', 'description')


class PlanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plante
        fields = ('id', 'lopin', 'nom', 'image', 'espece', 'description')


class ActualiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actualite
        fields = ('id', 'auteur', 'jardin', 'texte', 'date_creation')

