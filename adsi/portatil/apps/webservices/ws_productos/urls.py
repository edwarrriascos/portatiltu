from django.conf.urls.defaults import patterns, url

from django.conf.urls import include
from rest_framework import routers
from portatil.apps.webservices.ws_productos.views import *
router = routers.DefaultRouter()
router.register(r'marca', marca_viewset)
router.register(r'conectividad', conectividad_viewset)
router.register(r'accesorios', accesorios_viewset)
router.register(r'portatil', portatil_viewset)
urlpatterns = patterns('portatil.apps.webservices.ws_productos.views',
		url(r'^ws/productos/$','ws_productos_view',name = 'ws_productos_url'),
		url(r'^api/', include (router.urls)),
		url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework'))
		)