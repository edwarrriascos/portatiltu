# Create your views here.
#vistas de la aplicacion ventas
from django.shortcuts import render_to_response
from django.template import RequestContext
from portatil.apps.ventas.models import Portatil
from portatil.apps.home.forms import contact_form
from django.core.mail import EmailMultiAlternatives
from portatil.apps.home.forms import add_product_form, login_form
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def paginaprincipal_view(request):
	return render_to_response('home/paginaprincipal.html', context_instance = RequestContext(request))

def about_view(request):
	mensaje = " Analisis y Deasarrollo de Sistemas de Informacion"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html', ctx, context_instance = RequestContext(request))

def portatiles_view(request, pagina):
	lista_prod = Portatil.objects.filter(status = True)
	paginator  = Paginator(lista_prod, 3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage, InvalidPage):
		productos = paginator.page(paginator.num_pages)

	ctx  = {'portatiles':productos}
	return render_to_response('home/portatil.html', ctx, context_instance =RequestContext(request))

def contacto_view(request):
	info_enviado = False
	email = ""
	title = ""
	text  = ""
	if request.method == "POST":
		formulario = contact_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['correo']
			title = formulario.cleaned_data['titulo']
			text  = formulario.cleaned_data['texto']
			'''bloque de configuracion de envio por GMAIL'''
			to_admin = 'chisda@misena.edu.co'
			html_content = "informacion recibida de %s <br>---mensaje---<br> %s"%(email,text)
			msg = EmailMultiAlternatives('correo de contacto',html_content,'from@server.com',[to_admin])
			msg = attach_alternative(html_content, 'text/html')
			msg.send()
			'''Fin de bloque'''
	else:
		formulario = contact_form()
	ctx = {'form':formulario, 'email':email, "title":title, 'text':text, "info_enviado":info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))
	
def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)#se loguea al sistema con la informacion de usuario
					return HttpResponseRedirect('/')#redirigimos a la pagina principal
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = login_form()# creamos un formulario nuevo
		ctx = {'form':formulario, 'mensaje':mensaje}#variable para pasar informacion a login.html
		return render_to_response('home/login.html',ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def single_portatil_view(request, id_portatil):
	prod = Portatil.objects.get(id = id_portatil)
	ctx  = {'portatil':prod}
	return render_to_response('home/single_portatil.html',ctx,context_instance = RequestContext(request))
