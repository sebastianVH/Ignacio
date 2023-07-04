from django import forms
from .models import Trabajadore, Evento, ReservasMesa


# Importo las tablas de models.py con sus atributos a forms.py
class trabajadorFormularios(forms.ModelForm):
    class Meta:
        model = Trabajadore
        fields = '__all__'


class reservacionFormularios(forms.ModelForm):
    class Meta:
        model = ReservasMesa
        fields = '__all__'


class eventoFormularios(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
