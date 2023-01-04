from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.contrib.auth.decorators import login_required
from .models import Entrega
from backend.crm.models import Cliente
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import EntregaForm, EntregaitemForm
from backend.orcamento.models import Orcamento,OrcamentoItens
from backend.orcamento.forms import OrcamentoForm, OrcamentoItemsFormset, OrcamentoItensForm
from backend.produto.models import Categoria
from django.views.generic import CreateView, DetailView, ListView
import django_tables2 as tables
from django.utils.html import format_html

# Create your views here.

class ListEntrega(ListView,LRM):
    template_name = 'logistica/entrega.html'
    model = Orcamento
    context_object_name= 'entregas'
    
   
    
def ItensEntrega(request):
    dbs = Entrega.objects.all()
    context = {'db':dbs}
    return render(request, 'logistica/itens_entrega.html',context)

@login_required
def orcamento_create(request, client_pk):
    cliente = Cliente.objects.get(pk=client_pk)
    orcamento = Orcamento.objects.create(cliente=cliente)
    return redirect(reverse_lazy('orcamento:orcamento_update', kwargs={'pk': orcamento.pk}))  # noqa E501



 






