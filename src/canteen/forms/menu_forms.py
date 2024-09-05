from django import forms
from ..models.menu_model import MenuModel


class MenuForm(forms.ModelForm):

    class Meta:
        model = MenuModel
        fields = ['flat'] 
