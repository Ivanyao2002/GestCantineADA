from django import forms
from ..models.flat_model import FlatModel


class FlatForm(forms.ModelForm):

    class Meta:
        model = FlatModel
        fields = ['name', 'summary']


        labels ={
            'name': 'Nom du plat',
        }

        widgets ={
            'summary': forms.Textarea()
        }