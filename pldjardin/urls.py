"""pldjardin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers

from apps.commentaires.views import CommentaireJardinViewSet, CommentaireLopinViewSet, CommentairePlanteViewSet
from apps.gensdujardin.views import UserViewSet
from apps.jardin.views import JardinViewSet, AdresseViewSet, LopinViewSet, ActualiteViewSet, PlanteViewSet
from apps.actions.views import ActionViewSet, TypeActionViewSet


router = routers.DefaultRouter()
router.register(r'utilisateurs', UserViewSet )
router.register(r'jardins', JardinViewSet )
router.register(r'adresses', AdresseViewSet )
router.register(r'lopins', LopinViewSet)
router.register(r'actualites', ActualiteViewSet)
router.register(r'plantes', PlanteViewSet)
router.register(r'actions', ActionViewSet)
router.register(r'typesaction', TypeActionViewSet)
router.register(r'commentairesjardin', CommentaireJardinViewSet)
router.register(r'commentaireslopin', CommentaireLopinViewSet)
router.register(r'commentairesplante', CommentairePlanteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
