from django import forms

from .models import Entrega,Orcamento

class EntregaForm(forms.ModelForm):
   class Meta:
       model = Orcamento
       fields = '__all__'
       
class EntregaitemForm(forms.ModelForm):
       class Meta:
        model = Entrega
        fields = '__all__'
