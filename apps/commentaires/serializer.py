from rest_framework import serializers
from apps.commentaires.models import CommentairePlante, CommentaireLopin, CommentaireJardin, Commentaire

"""
    Serializers basiques
"""


class CommentairePlanteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CommentairePlante
        fields = ('id', 'texte', 'date_creation', 'utilisateur', 'plante')


class CommentaireLopinSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CommentaireLopin
        fields = ('id', 'texte', 'date_creation', 'utilisateur', 'lopin')


class CommentaireJardinSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CommentaireJardin
        fields = ('id', 'texte', 'date_creation', 'utilisateur', 'jardin')
