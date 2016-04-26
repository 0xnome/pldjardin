from rest_framework import viewsets
from apps.jardin.models import Jardin
from apps.jardin.serializers import JardinSerializer

class JardinViewSet(viewsets.ModelViewSet):
    """
        list, create, retreive, update and delete
    """
    queryset = Jardin.objects.all()
    serializer_class = JardinSerializer
