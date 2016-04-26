from rest_framework import viewsets
from apps.jardin.models import Jardin, Adresse, Lopin, Actualite, Plante
from apps.jardin.serializers import JardinSerializer, AdresseSerializer, LopinSerializer, ActualiteSerializer, \
    PlanteSerializer


class JardinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
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
    queryset = Lopin.objects.all()
    serializer_class = LopinSerializer

class ActualiteViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = Actualite.objects.all()
    serializer_class = ActualiteSerializer

class PlanteViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = Plante.objects.all()
    serializer_class = PlanteSerializer

