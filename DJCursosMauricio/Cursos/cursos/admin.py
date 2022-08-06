
from typing import Optional, Sequence
from django.contrib import admin
from .models import Archivos, ComentarioContacto, Cursos

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

class AdministartModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('NombreCurso', 'FechaInicio' ,'Descripcion', 'AlumnosRegistrados')
    search_fields: Sequence[str] = ('NombreCurso', 'FechaInicio' ,'Descripcion', 'AlumnosRegistrados')
    date_hierarchy: Optional[str] = 'created'
    list_filter = ('NombreCurso','AlumnosRegistrados')

    def get_readonly_fields(self, request, obj=None):
#si el usuario pertenece al grupo de permisos "Usuario"
        if request.user.groups.filter(name="Usuarios").exists():
#Bloquea los campos
            return ('NombreCurso', 'NombreTutor', 'Descripcion', 'Platafroma')
#Cualquier otro usuario que no pertenece al grupo "Usuario"
        else:
#Bloquea los campos
            return ('created', 'update')
    
admin.site.register(Cursos, AdministartModelo)


class AdministrarContacto(admin.ModelAdmin):
    list_display = ('id','nombre', 'email', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Archivos, AdministrarContacto)


