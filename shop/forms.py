from django import forms
from .models import ColorModel, ProductModel


class ColorModelForm(forms.ModelForm):
    code = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'type': 'color'}),)

    class Meta:
        model = ColorModel
        fields = '__all__'

class ProductModelModelForm(forms.ModelForm):
    color = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'type': 'color'}),)

    class Meta:
        model = ProductModel
        fields = ['color']