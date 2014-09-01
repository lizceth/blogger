from django.contrib import admin
from django.contrib.auth.models import User
from usuarios.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['nombre','apellido_pat','apellido_mat','sexo','E_mail']

admin.site.register(Usuario, UsuarioAdmin)
