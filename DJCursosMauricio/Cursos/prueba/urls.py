"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contenido import views
from django.conf import settings
from cursos import views as views_registros

urlpatterns = [
    # URLS de Los Views
    path('admin/', admin.site.urls),
    path('',views.principal,name='Principal'),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('cursos/',views_registros.registros, name='Cursos'),
    path('comentario/',views_registros.comentario,name='Comentario'),
    path('consultaContacto/',views_registros.consultaContacto,name='ConsultaContacto'),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('formEditarComentario/<int:id>/',views_registros.consultarComentarioIndividual,name='ConsultaIndividual'),
    path('editarComentario/<int:id>/',views_registros.editarComentarioContacto, name='Editar'),
    path('contacto/',views_registros.archivos,name='Contacto'),
    path('consultasSQL/',views_registros.consultasSQL,name='ConsultaSQL'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
