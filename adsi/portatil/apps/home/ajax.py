import random
from dajax.core import Dajax 
from dajaxice.decorators import dajaxice_register

@dajaxice_register

def randomize(request):
	dajax = Dajax()
	dajax.assing('#result', 'value', random.randint(1,10))
	return dajax.json()
	from dajax.core import Dajax
	
@dajaxice_register
def updatecombo(request, option):
    dajax = Dajax()
    options = [['Madrid', 'Barcelona', 'Vitoria', 'Burgos'],
               ['Paris', 'Evreux', 'Le Havre', 'Reims'],
               ['London', 'Birmingham', 'Bristol', 'Cardiff']]
    out = []
    for option in options[int(option)]:
        out.append("<option value='#'>%s</option>" % option)

    dajax.assign('#combo2', 'innerHTML', ''.join(out))
    return dajax.json()