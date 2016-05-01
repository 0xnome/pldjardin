from rest_framework import serializers
from apps.commentaires.models import CommentairePlante, CommentaireLopin, CommentaireJardin, Commentaire

"""
    Serializers basiques
"""


class CommentairePlanteFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentairePlante
        fields = ('id', 'texte', 'date_creation', 'auteur', 'plante')


class CommentairePlanteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentairePlante
        fields = ('id', 'texte', 'plante')


class CommentaireLopinFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireLopin
        fields = ('id', 'texte', 'date_creation', 'auteur', 'lopin')


class CommentaireLopinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireLopin
        fields = ('id', 'texte', 'lopin')


class CommentaireJardinFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireJardin
        fields = ('id', 'texte', 'date_creation', 'auteur', 'jardin')


class CommentaireJardinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireJardin
        fields = ('id', 'texte', 'jardin')
