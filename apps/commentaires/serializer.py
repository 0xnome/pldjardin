from rest_framework import serializers
from apps.commentaires.models import CommentairePlante, CommentaireLopin, CommentaireJardin, Commentaire

"""
    Serializers basiques
"""


class CommentairePlanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentairePlante
        fields = ('id', 'texte', 'date_creation', 'utilisateur', 'plante')


class CommentaireLopinSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentaireLopin
        fields = ('id', 'texte', 'date_creation', 'utilisateur', 'lopin')


class CommentaireJardinSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentaireJardin
        fields = ('id', 'texte', 'date_creation', 'utilisateur', 'jardin')
