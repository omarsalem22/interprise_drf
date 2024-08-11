from django import forms
from .models import Product

class ProdeuctForm(forms.ModelForm):
     class Meta:
          model=Product
          fields=[
               'title',
               'content',
               'price'
          ]
      