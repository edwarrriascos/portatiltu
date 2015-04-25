# Create your views here.
from django.http import HttpResponse
from portatil.apps.ventas.models import *
from django.core import serializers


def ws_productos_view(request):
	data = serializers.serialize("json", Portatil.objects.filter(status = True))
	return HttpResponse(data, mimetype='application/json')
	
from serializer import *
from rest_framework import viewsets

class marca_viewset(viewsets.ModelViewSet):
	queryset = Marca.objects.all()
	serializer_class = marca_serializer

class conectividad_viewset (viewsets.ModelViewSet):
	queryset = Conectividad.objects.all()
	serializer_class = conectividad_serializer

class accesorios_viewset (viewsets.ModelViewSet):
	queryset = Accesorios.objects.all()
	serializer_class = accesorios_serializer

class portatil_viewset (viewsets.ModelViewSet):
	queryset = Portatil.objects.all()
	serializer_class = portatil_serializer

