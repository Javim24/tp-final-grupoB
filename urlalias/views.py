from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import URLForm2
from .models import URLAlias
import nanoid

# Create your views here.
_NANO_DICT = "abcdefz-"

def index(request):


    if request.method == "POST":
        # Se puede acceder a la informacion del POST de forma
        form = URLForm2(request.POST)
        if form.is_valid():
            fullurl = form.cleaned_data.get("fullurl")
            url = URLAlias(fullurl=fullurl)
            alias = nanoid.generate(size=5)
            url.alias=alias
            url.save()
            ctx  = {"title": "Bienvenido al url alias", "url": fullurl, "alias": alias}
            return render(request, "urlalias/registrado.html", ctx)
        else:
            return HttpResponse("El formulario es invalido") 
    
    form = URLForm2()

    ctx  = {"title": "Bienvenido al url alias", "form": form}
	

    return render(request, "urlalias/home.html", ctx)

def resolve_alias(request, alias):
    resultado = URLAlias.objects.get(alias=alias)
    resultado.visitas += 1
    resultado.save()

    # return HttpResponse(f"La URL para el alias {alias} es {resultado.fullurl}")
    return HttpResponseRedirect(resultado.fullurl) 

