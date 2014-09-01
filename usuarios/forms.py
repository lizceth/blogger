# coding:utf-8
from django.forms import ModelForm
from django import forms
from usuarios.models import  Usuario


class UsuarioForm(ModelForm):
     class Meta:
         model = Usuario

