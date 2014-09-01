#coding:utf-8
from django.db import models
from usuarios.models import Usuario

CATEGORIA=(
    ('Academico', 'Academico'),
    ('Tecnologico', 'Tecnologico'),
    ('Noticias', 'Noticias'),
    ('Deportes', 'Deportes'),
    ('Espiritual', 'Espiritual'),
    ('Social', 'Social'),

)

class Articulo(models.Model):
    autor=models.ForeignKey(Usuario)
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    fecha_pub=models.DateTimeField(auto_now_add=True)
    categoria=models.CharField(max_length=11, choices=CATEGORIA)
    imagen=models.ImageField(upload_to='articulos', verbose_name='Imágen')
    def __unicode__(self):
        return self.titulo

    class Meta:
        ordering=['fecha_pub']

class Comentario(models.Model):
    articulo=models.ManyToManyField(Articulo)
    texto=models.TextField()
    fecha=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['fecha']
