from rest_framework import serializers

from apps.jardin.models import Jardin, Adresse, Lopin, Actualite, Plante


"""
    Serializers basiques
"""

class AdresseFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = ('id', 'ville', 'code_postal', 'rue', 'long', 'lat', 'jardins', 'lopins')

class AdresseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = ('id', 'ville', 'code_postal', 'rue', 'long', 'lat')


class JardinFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'actualites', 'lopins', 'commentaires', 'site', 'contact', 'horaire', 'image', 'description', 'restreint', 'composteur', 'adresse', 'administrateurs', 'membres')


class JardinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'site', 'contact', 'horaire', 'image', 'description', 'restreint', 'composteur', 'adresse')


class JardinUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'site', 'contact', 'horaire', 'image', 'description', 'restreint', 'composteur', 'adresse', 'administrateurs', 'membres')


class LopinFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lopin
        fields = ('id', 'adresse', 'jardin', 'nom', 'description')


class LopinUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lopin
        fields = ('id', 'adresse', 'nom', 'description')


class PlanteFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plante
        fields = ('id', 'lopin', 'nom', 'image', 'espece', 'description')

class PlanteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plante
        fields = ('id', 'nom', 'image', 'espece', 'description')


class ActualiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actualite
        fields = ('id', 'auteur', 'jardin', 'texte', 'date_creation')

"""
class AdresseFullWithSerializer(AdresseFullSerializer):
    jardins = JardinFullSerializer(many=True)
    lopins = LopinFullSerializer(many=True)
"""

class AdresseFullWithSerializer(AdresseFullSerializer):
    jardins = JardinFullSerializer(many=True)
    lopins = LopinFullSerializer(many=True)


class ResultsSerializer(serializers.Serializer):
    jardins = JardinFullSerializer(many=True, read_only=True)
    lopins = LopinFullSerializer(many=True, read_only=True)
    plantes = PlanteFullSerializer(many=True, read_only=True)
    # adresses = AdresseFullWithSerializer(many=True, read_only=True)
