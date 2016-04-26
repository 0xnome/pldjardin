from rest_framework import viewsets

from apps.actions.models import Action, TypeAction
from apps.actions.serializers import ActionSerializer, TypeActionSerializer


class ActionViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class TypeActionViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = TypeAction.objects.all()
    serializer_class = TypeActionSerializer
