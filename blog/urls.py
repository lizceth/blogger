from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'articulos.views.inicio'),
    url(r'^detalle/(?P<id_articulo>\d+)$', 'articulos.views.detalle'),
    url(r'^agregar/articulo/$', 'articulos.views.agregar_articulo'),
    url(r'^editar/articulo/(?P<id>\d+)$', 'articulos.views.editar_articulo'),
    url(r'^borrar/articulo/(?P<id>\d+)$', 'articulos.views.borrar_articulo'),
    url(r'^sobre/$', 'articulos.views.sobre'),

    url(r'^articulos/$', 'articulos.views.articulos'),
    url(r'^ingresar/$', 'usuarios.views.ingresar'),
    url(r'^index/(?P<id>\d+)$', 'usuarios.views.index'),
    url(r'^privado/$', 'usuarios.views.privado'),
    url(r'^cerrar/$', 'usuarios.views.cerrar'),

)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
