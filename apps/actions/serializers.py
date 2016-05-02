from rest_framework import serializers
from apps.actions.models import Action

"""
    Serializers basiques
"""

class ActionFullSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'type', 'utilisateur',
                  #'lopin',
                  'plante', 'date_creation')
        model = Action

class ActionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'type',
                  #'lopin',
                  'plante')
        model = Action

    def validate(self, data):
        # verification que le type est autorisé
        type = data["type"] if "type" in data else (self.instance.type if self.instance else "")

        if not type in Action.USER_AVAILABLE_ACTION:
            raise serializers.ValidationError(
                {"type": "Ce type d'action n'est pas autorisé"})
        return data