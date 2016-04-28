from rest_framework import serializers
from apps.actions.models import Action, TypeAction

"""
    Serializers basiques
"""


class TypeActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeAction
        fields = ('id', 'nom')


class ActionSerializer(serializers.ModelSerializer):
    type_action = TypeActionSerializer(many=False)

    class Meta:
        fields = ('id', 'type_action', 'utilisateur', 'lopin', 'plante', 'date_creation')
        model = Action

