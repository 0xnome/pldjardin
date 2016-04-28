from rest_framework import viewsets

from apps.actions.models import Action, TypeAction
from apps.actions.serializers import ActionSerializer, TypeActionSerializer
from apps.actions.permissions import ActionPermission

class ActionViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    permission_classes = (ActionPermission,)
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class TypeActionViewSet(viewsets.ReadOnlyModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = TypeAction.objects.all()
    serializer_class = TypeActionSerializer
