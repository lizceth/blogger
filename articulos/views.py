from django.shortcuts import render, render_to_response, get_object_or_404
from articulos.models import Articulo, Comentario
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from articulos.forms import ArticuloForm,  ComentarioForm

def inicio(request):
    articulos=Articulo.objects.order_by('fecha_pub')
    return render_to_response('index.html',
                              {'articulos':articulos},
                              context_instance=RequestContext(request))

def detalle(request, id_articulo):
    articulo = get_object_or_404(Articulo, pk=id_articulo)
    comentarios = Comentario.objects.filter(articulo=articulo)
    return render_to_response('articulos/detalle.html',
                              {'articulo':articulo,'comentarios':comentarios}, context_instance=RequestContext(request))


def sobre(request):
    titulo = 'blog academico FIA'
    return render(request, 'articulos/sobre.html',
                  {'titulo':titulo})
def articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'usuarios/articulo.html',
                  {'articulos':articulos})


def editar_articulo(request, id):
        editar_articulo= Articulo.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ArticuloForm(request.POST, instance = editar_articulo)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/articulos/")
        else:
            formulario = ArticuloForm(instance= editar_articulo)
        return render_to_response('articulos/editar_articulo.html',
                                 {'formulario': formulario},
                                  context_instance = RequestContext(request))

def agregar_articulo(request):
    if request.method == 'POST':
        formulario = ArticuloForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/articulos/')
    else:
        formulario = ArticuloForm()
    return render_to_response('articulos/articuloform.html',
                              {'formulario':formulario},
                          context_instance=RequestContext(request))

def borrar_articulo(request, id):
    borrar_articulo = get_object_or_404(Articulo, pk=id)
    borrar_articulo.delete()
    return HttpResponseRedirect("/articulos/")
