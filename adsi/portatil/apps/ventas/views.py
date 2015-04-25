# Create your views here.  
from django.shortcuts import render_to_response
from django.template import RequestContext
from portatil.apps.home.forms import add_product_form
from portatil.apps.ventas.models import Portatil
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save()
			formulario.save_m2m()
			info = "se guardo satisfactoriamente"
			return HttpResponseRedirect('/portatil/%s'%add.id)
	else:
		formulario = add_product_form()
	ctx = {'form':formulario, 'info':info}
	return render_to_response('ventas/add_producto.html',ctx, context_instance = RequestContext(request))

def edit_producto_view(request, id_prod):
	info = ""
	prod = Portatil.objects.get(pk = id_prod)

	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES, instance= prod)
		if formulario.is_valid():
			edit_prod = formulario.save(commit = False)
			formulario.save_m2m()
			edit_prod.status = True			
			edit_prod.save()
			info = "se guardo satisfactoriamente"				
			return HttpResponseRedirect('/portatil/%s'%edit_prod.id)
	else:
		formulario = add_product_form(instance = prod)
		
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/edit_producto.html',ctx ,context_instance = RequestContext(request))
