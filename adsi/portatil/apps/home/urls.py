from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('portatil.apps.home.views',
	    url(r'^$','paginaprincipal_view', name = 'vista_principal'),    
	    url(r'^about/$', 'about_view', name = 'vista_about'),
	    url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),
	    url(r'^login/$', 'login_view', name = 'vista_login'),
	    url(r'^logout/$', 'logout_view', name = 'vista_logout'),
	    url(r'^portatiles/page/(?P<pagina>.*)/$','portatiles_view', name = 'vista_portatiles'),
		url(r'^portatil/(?P<id_portatil>.*)/$', 'single_portatil_view', name = 'vista_portatil'),
	)	    