from rest_framework import generics
from apps.jardin.models import Jardin

from apps.jardin.serializers import JardinSerializer


class JardinList(generics.ListAPIView):
    queryset = Jardin.objects.all()
    serializer_class = JardinSerializer


class JardinDetail(generics.RetrieveAPIView):
    queryset = Jardin.objects.all()
    serializer_class = JardinSerializer