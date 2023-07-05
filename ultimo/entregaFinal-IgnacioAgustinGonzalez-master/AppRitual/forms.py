from django import forms
from .models import Trabajadore, Evento, ReservasMesa


# Importo las tablas de models.py con sus atributos a forms.py
class trabajadorFormularios(forms.ModelForm):
    class Meta:
        model = Trabajadore
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'formInput'}),
            'apellido': forms.TextInput(attrs={'class': 'formInput'}),
            'sector': forms.TextInput(attrs={'class': 'formInput'}),
            'telefono': forms.TextInput(attrs={'class': 'formInput'}),
            'email': forms.EmailInput(attrs={'class': 'formInput'}),
            'fechaContratacion': forms.DateInput(attrs={'class': 'formInput'}),
            'salario': forms.NumberInput(attrs={'class': 'formInput'}),
            'foto_id': forms.FileInput(attrs={'class': 'formInput'}),
            'anotaciones': forms.Textarea(attrs={'rows': 2, 'cols': 25}),
        }


class reservacionFormularios(forms.ModelForm):
    class Meta:
        model = ReservasMesa
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'formInput'}),
            'apellido': forms.TextInput(attrs={'class': 'formInput'}),
            'fechaSolicitud': forms.DateInput(attrs={'class': 'formInput'}),
            'fechaReserva': forms.DateInput(attrs={'class': 'formInput'}),
            'horaReserva': forms.TimeInput(attrs={'class': 'formInput'}),
            'numeroPersonas': forms.NumberInput(attrs={'class': 'formInput'}),
            'telefono': forms.TextInput(attrs={'class': 'formInput'}),
            'email': forms.EmailInput(attrs={'class': 'formInput'}),
            'estado': forms.CheckboxInput(attrs={'class': 'formInput'}),
            'anotaciones': forms.Textarea(attrs={'rows': 2, 'cols': 25}),
        }

class eventoFormularios(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
