from rest_framework import viewsets, mixins

from apps.actions.models import Action, TypeAction
from apps.actions.serializers import ActionSerializer, TypeActionSerializer
from apps.actions.permissions import ActionPermission
from rest_framework import permissions

class ActionViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (ActionPermission,)
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class TypeActionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TypeAction.objects.all()
    serializer_class = TypeActionSerializer
