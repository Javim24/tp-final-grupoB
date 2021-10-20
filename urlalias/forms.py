from django import forms
from .models import URLAlias

class URLForm(forms.ModelForm):
    # created_at = forms.DateField(label="Fecha de inicio", 
    #    widget=forms.DateInput(attrs={"type": "date"}, format='%d/%m/%Y'),
    #    input_formats=('%d/%m/%Y', ))
    fullurl = forms.CharField(label="Ingrese la url a convertir")
    # alias = forms.CharField(label="alias")
    class Meta:
        model = URLAlias
        fields = ['fullurl']

class URLForm2(forms.Form):
    fullurl = forms.CharField(label="Ingrese la url a convertir")
