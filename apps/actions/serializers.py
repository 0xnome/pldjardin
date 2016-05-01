from rest_framework import serializers
from apps.actions.models import Action

"""
    Serializers basiques
"""

class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'type', 'utilisateur',
                  #'lopin',
                  'plante', 'date_creation')
        model = Action

