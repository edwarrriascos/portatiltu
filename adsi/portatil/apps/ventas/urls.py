from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('portatil.apps.ventas.views',
		url(r'^add/portatil/$','add_product_view',name = 'vista_agregar_producto'),
		url(r'^edit/portatil/(?P<id_prod>.*)/$','edit_producto_view', name = 'vista_editar_producto'),
	)

