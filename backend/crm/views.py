from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import redirect, render

from .forms import ClienteForm, FornecedorForm
from .models import Cliente, Fornecedor


class ClienteListView(LRM, ListView):
    model = Cliente


class ClienteDetailView(LRM, DetailView):
    model = Cliente


class ClienteCreateView(LRM, CreateView):
    model = Cliente
    form_class = ClienteForm

def cliente_update(request, pk):
    template_name = 'crm/cliente_form.html'
    cliente_instance = Cliente.objects.get(pk=pk)

    form = ClienteForm(request.POST or None, instance=cliente_instance, prefix='main')  # noqa E501

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('crm:cliente_list')

    context = {
        'form': form,
    }
    return render(request, template_name, context)

def cliente_delete(request, pk):
    order_item = Cliente.objects.get(pk=pk)
    order_item.delete()
    return redirect('crm:cliente_list')

class FornecedorListView(LRM, ListView):
    model = Fornecedor


class FornecedorDetailView(LRM, DetailView):
    model = Fornecedor


class FornecedorCreateView(LRM, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    
def fornecedor_update(request, pk):
    template_name = 'crm/fornecedor_form.html'
    fornecedor_instance = Fornecedor.objects.get(pk=pk)

    form = FornecedorForm(request.POST or None, instance=fornecedor_instance, prefix='main')  # noqa E501

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('crm:fornecedor_list')

    context = {
        'form': form,
    }
    return render(request, template_name, context)

def fornecedor_delete(request, pk):
    order_item = Fornecedor.objects.get(pk=pk)
    order_item.delete()
    return redirect('crm:fornecedor_list')
