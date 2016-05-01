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

class jardinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jardin

    def validate(self, data):
        # verification que les admins sont des membres
        membres = data["membres"] if "membres" in data else (self.instance.membres.all() if self.instance else [])
        administrateurs = data["administrateurs"] if "administrateurs" in data else (self.instance.administrateurs.all() if self.instance else [])

        if not set(administrateurs) <= set(membres):
            raise serializers.ValidationError({"administrateurs":"Les administrateurs doivent être membre du jardin !"})
        return data


class JardinFullSerializer(jardinSerializer):
    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'actualites', 'lopins', 'commentaires', 'site', 'contact', 'horaire', 'image', 'description', 'restreint', 'composteur', 'adresse', 'administrateurs', 'membres')


class JardinCreateSerializer(jardinSerializer):
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


class JardinUpdateSerializer(jardinSerializer):
    class Meta:
        model = Jardin
        fields = ('id', 'nom', 'site', 'contact', 'horaire', 'image', 'description', 'restreint', 'composteur', 'administrateurs', 'membres')


class LopinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lopin

    def validate(self, attrs):
        # verification : si le lopin a un jardin, son adresse doit  etre la meme que le jardin
        jardin = attrs["jardin"] if "jardin" in attrs else (self.instance.jardin if self.instance else None)
        adresse = attrs["adresse"] if "adresse" in attrs else (self.instance.adresse if self.instance else None)
        if jardin is None and adresse is None:
            raise serializers.ValidationError({"jardin":"Un lopin doit avoir un jardin, ou une adresse.","adresse":"Un lopin doit avoir un jardin, ou une adresse."})
        if jardin is not None and (adresse != jardin.adresse and adresse is not None):
            raise serializers.ValidationError({"adresse":"L'adresse d'un lopin appartenant a un jardin, doit être celle du jardin"})
        return attrs

class LopinFullSerializer(LopinSerializer):
    class Meta:
        model = Lopin
        fields = ('id', 'adresse', 'jardin', 'nom', 'description')


class LopinCreateSerializer(LopinSerializer):
    adresse = AdresseCreateSerializer(required=False, allow_null=True)

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
            lopin.save()
        return lopin

class LopinUpdateSerializer(LopinSerializer):
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


class ActualiteFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actualite
        fields = ('id', 'auteur', 'jardin', 'texte', 'date_creation')

class ActualiteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actualite
        fields = ('id', 'jardin', 'texte')

class AdresseFullWithSerializer(AdresseFullSerializer):
    jardins = JardinFullSerializer(many=True)
    lopins = LopinFullSerializer(many=True)


class ResultsSerializer(serializers.Serializer):
    jardins = JardinFullSerializer(many=True, read_only=True)
    lopins = LopinFullSerializer(many=True, read_only=True)
    plantes = PlanteFullSerializer(many=True, read_only=True)
    # adresses = AdresseFullWithSerializer(many=True, read_only=True)
