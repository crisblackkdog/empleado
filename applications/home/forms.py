from django import forms

from applications.home.models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""
    class Meta:
        """Meta definition for Pruebaform."""
        model = Prueba
        fields = ('titulo',
                  'subtitulo',
                  'cantidad'
        )
        widgets ={
            'titulo' : forms.TextInput(
                attrs = {
                    'placeholder': 'ingrese texto',
                }
            )
        }
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Debe ingresar mayor a 10')
        return cantidad