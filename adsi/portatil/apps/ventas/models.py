from django.db import models
from django.conf.urls.defaults import url

# Create your models here.

class Marca (models.Model):
	nombre_marca		= models.CharField(max_length = 100)

	def __unicode__ (self):
		return self.nombre_marca

class Conectividad (models.Model):
	nombre_conectividad		= models.CharField(max_length = 100)

	def __unicode__ (self):
		return self.nombre_conectividad

class Accesorios (models.Model):
	nombre			= models.CharField(max_length = 50)
	descripcion		= models.CharField(max_length = 200)

	def __unicode__ (self):
		return self.nombre

class Portatil (models.Model):

	def url(self, filename):
		ruta = "MultimediaData/Portatil/%s/%s"%(self.referencia,str(filename))
		return ruta

	marca 			= models.ForeignKey(Marca)
	conectividad    = models.ManyToManyField(Conectividad)
	accesorios   	= models.ManyToManyField(Accesorios)
	color			= models.CharField(max_length = 100)
	serial			= models.CharField(max_length = 50)
	referencia		= models.CharField(max_length = 50)
	procesador		= models.CharField(max_length = 50)
	imagen			= models.ImageField(upload_to = url, null = True, blank = True)
	memoria_ram		= models.CharField(max_length = 50)
	sistema_operativo	= models.CharField(max_length = 50)
	status			= models.BooleanField(default = True)

	def __unicode__ (self):
		return self.marca.nombre_marca
	