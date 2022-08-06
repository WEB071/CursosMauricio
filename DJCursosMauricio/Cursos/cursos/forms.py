from django import forms
from .models import Archivos, ComentarioContacto



class CustomClearableFieldInput(forms.ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'



class FormArchivos(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = ('nombre', 'mensaje', 'email','telefono', 'archivo')
        widgets = {
            'archivo': CustomClearableFieldInput
        }

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario','mensaje']