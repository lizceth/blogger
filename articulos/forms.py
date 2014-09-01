# coding:utf-8
from django.forms import ModelForm
from django import forms
from articulos.models import Articulo, Comentario

class ArticuloForm(ModelForm):
     class Meta:
         model = Articulo


class ComentarioForm(ModelForm):
     class Meta:
         model = Comentario
