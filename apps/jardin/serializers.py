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


class AdresseCreateSerializer(AdresseUpdateSerializer):
    pass


class JardinFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'actualites', 'lopins', 'commentaires', 'site', 'contact', 'horaire', 'image', 'description', 'restreint', 'composteur', 'adresse', 'administrateurs', 'membres')


class JardinCreateSerializer(serializers.ModelSerializer):
    adresse = AdresseCreateSerializer(many=False)

    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'site', 'contact', 'horaire', 'image', 'description', 'restreint', 'composteur', 'adresse')
        depth = 1

    def create(self, validated_data):
        adresse = Adresse.objects.create(**validated_data.pop('adresse'))
        adresse.save()
        membres = administrateurs = None
        if("administrateurs" in validated_data):
            administrateurs = validated_data.pop('administrateurs')
        if("membres" in validated_data):
            membres = validated_data.pop('membres')

        jardin = Jardin.objects.create(adresse=adresse, **validated_data)

        if("administrateurs" is not None):
            jardin.administrateurs.add(*administrateurs)
        if("membres" is not None):
            jardin.membres.add(*membres)

        return jardin


class JardinUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'site', 'contact', 'horaire', 'image', 'description', 'restreint', 'composteur', 'administrateurs', 'membres')


class LopinFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lopin
        fields = ('id', 'adresse', 'jardin', 'nom', 'description')


class LopinCreateSerializer(serializers.ModelSerializer):
    adresse = AdresseCreateSerializer(required=False)

    class Meta:
        model = Lopin
        fields = ('id', 'adresse', 'jardin', 'nom', 'description')


    def create(self, validated_data):
        if('adresse' in validated_data and validated_data["adresse"] != "" and validated_data["adresse"] is not None):
            adresse = Adresse.objects.create(**validated_data.pop('adresse'))
            adresse.save()

            lopin = Lopin.objects.create(adresse=adresse, **validated_data)
        else:
            # alors le jardin est set
            lopin = Lopin.objects.create(**validated_data)
            lopin.adresse = lopin.jardin.adresse

        return lopin

class LopinUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lopin
        fields = ('id', 'nom', 'description')


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
