from django import forms

class SectorFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   codigo = forms.IntegerField(required=True, max_value=50000)

class JefeFormulario(forms.Form):
   apellido = forms.CharField(required=True, max_length=256)
   nombre = forms.CharField(required=True, max_length=64)
   dni = forms.CharField(required=True, max_length=32)
   email = forms.CharField(required=True)
   fecha_nacimiento = forms.DateField(required=True)
   profesion = forms.CharField(max_length=128)
 
