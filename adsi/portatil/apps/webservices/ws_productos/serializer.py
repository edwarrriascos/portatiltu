from rest_framework import serializers
from portatil.apps.ventas.models import Marca, Conectividad, Accesorios, Portatil

class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marca
		fields = ('url','nombre_marca')


class conectividad_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Conectividad
		fields = ('url','nombre_conectividad')

class accesorios_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Accesorios
		fields =  ('url','nombre','descripcion')

class portatil_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Portatil
		fields = ('url','color','serial','sistema_operativo')