from django.db import models
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextField



class Cursos(models.Model): #Define la estructura de la tabla
    
    NombreCurso = models.CharField(max_length=100, verbose_name="Curso") #Define el tipo de dato y el tamaño
    Descripcion = models.TextField()
    AlumnosRegistrados = models.CharField(null=True, max_length=100, verbose_name="Alumnos Registrados")
    FechaInicio = models.CharField(null=True, max_length=100, verbose_name="Fecha de Inicio")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Imagen del Curso")
    created = models.DateTimeField(auto_now_add=True) #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True) #Fecha de actualizacion
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
    def __str__(self):
        return self.NombreCurso 
    

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]
    def __str__(self):
        return self.mensaje
#Indica que se mostrára el mensaje como valor en la tabla


class Archivos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(null=True, max_length=100, verbose_name="Nombre")
    email = models.CharField(null=True, max_length=100, verbose_name="Correo")
    mensaje = models.TextField(null=True, verbose_name="Mensaje")
    telefono = models.CharField(null=True, max_length=100, verbose_name="Telefono")
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    update  = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contacto"
        ordering = ["-created"]
        
        def __str__(self):
            return self.archivo