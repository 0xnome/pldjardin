from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from apps.gensdujardin.models import Utilisateur

from apps.gensdujardin.serializers import UtilisateurSerializer, UserSerializer


class UtilisateurList(generics.ListAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class UtilisateurDetail(generics.RetrieveAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer