from django import forms
from .models import Product, User


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('flag', 'name', 'type', 'count', 'whose')
        widghts = {
            'flag': forms.TextInput(attrs={'placeholder': '記入例:2019男子西医体一日目'}),
            'name': forms.TextInput(attrs={'placeholder': '記入例:水２L'}),
            'type': forms.RadioSelect(),
            'count': forms.NumberInput(attrs={'min': 1}),
            'whose': forms.ModelChoiceField(User.objects, ),

        }

