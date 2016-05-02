from rest_framework import viewsets, mixins

from apps.actions.models import Action
from apps.actions.serializers import ActionFullSerializer, ActionCreateSerializer
from apps.actions.permissions import ActionPermission

class ActionViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (ActionPermission,)
    queryset = Action.objects.all()

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(utilisateur=current_user)

    def get_serializer_class(self):
        if self.action == "create":
            return ActionCreateSerializer
        else:
            return ActionFullSerializer


