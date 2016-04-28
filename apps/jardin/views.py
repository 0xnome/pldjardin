from rest_framework import viewsets

from apps.jardin import permissions
from apps.jardin.models import Jardin, Adresse, Lopin, Actualite, Plante
from apps.jardin.serializers import JardinSerializer, AdresseSerializer, LopinSerializer, ActualiteSerializer, \
    PlanteSerializer
from apps.jardin.permissions import JardinPermission, LopinPermission, PlantePermission, ActualitePermission


class JardinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """

    permission_classes = (JardinPermission,)
    queryset = Jardin.objects.all()
    serializer_class = JardinSerializer


class AdresseViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """

    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer


class LopinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """

    permission_classes = (LopinPermission,)
    queryset = Lopin.objects.all()
    serializer_class = LopinSerializer


class ActualiteViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    permission_classes = (ActualitePermission,)
    queryset = Actualite.objects.all()
    serializer_class = ActualiteSerializer


class PlanteViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """

    permission_classes = (PlantePermission,)
    queryset = Plante.objects.all()
    serializer_class = PlanteSerializer

