from rest_framework import viewsets, mixins

from apps.actions.models import Action
from apps.actions.serializers import ActionSerializer
from apps.actions.permissions import ActionPermission

class ActionViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (ActionPermission,)
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

