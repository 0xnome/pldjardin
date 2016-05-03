from django.http import HttpResponse
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import list_route
from rest_framework.renderers import JSONRenderer

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

    @list_route(methods=["GET"])
    def types(self, request):
        # retourner les paire clé/valeur des types d'action disponible a la création pour un utilisateur
        res = {"types": []}
        for type in Action.ALL_ACTION:
            if type[0] in Action.USER_AVAILABLE_ACTION:
                res["types"].append(type)
        return HttpResponse(JSONRenderer().render(res), content_type="application/json", status=status.HTTP_200_OK)


    @list_route(methods=["GET"])
    def toustypes(self, request):
        # retourner les paire clé/valeur des types d'action disponible a la création pour un utilisateur
        res = {"types": {}}
        for type in Action.ALL_ACTION:
                res["types"][type[0]] = type[1]
        return HttpResponse(JSONRenderer().render(res), content_type="application/json", status=status.HTTP_200_OK)

