from django import forms
from portatil.apps.ventas.models import Portatil

class contact_form(forms.Form):
	correo	= forms.EmailField(widget = forms.TextInput())
	titulo	= forms.CharField(widget = forms.TextInput())
	texto	= forms.CharField(widget = forms.Textarea())

'''class add_product_form(forms.Form):
	nombre		= forms.CharField(widget = forms.TextInput())
	descripcion	= forms.CharField(widget = forms.Textarea())
	imagen		= forms.ImageField(required = False)
	precio		= forms.DecimalField(required = True)
	stock		= forms.IntegerField(required = True)
	def clean(self):
		return self.cleaned_data'''

class add_product_form(forms.ModelForm):
	class Meta:

		model = Portatil
		exclude = {'status',}

class login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())
	clave   = forms.CharField(widget = forms.PasswordInput(render_value = False))	
		