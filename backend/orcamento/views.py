from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from backend.crm.models import Cliente
from backend.produto.models import Produto

from .forms import OrcamentoForm, OrcamentoItemsFormset, OrcamentoItensForm, EntregaForm
from .models import Contrato, Orcamento


class OrcamentoListView(LRM, ListView):
    model = Orcamento


class OrcamentoDetailView(LRM, DetailView):
    model = Orcamento


@login_required
def orcamento_create(request, client_pk):
    cliente = Cliente.objects.get(pk=client_pk)
    orcamento = Orcamento.objects.create(cliente=cliente)
    return redirect(reverse_lazy('orcamento:orcamento_update', kwargs={'pk': orcamento.pk}))  # noqa E501


@login_required
def orcamento_update(request, pk):
    template_name = 'orcamento/orcamento_form.html'
    orcamento_instance = Orcamento.objects.get(pk=pk)

    if orcamento_instance.status == 'f':
        # Se orçamento estiver 'Finalizado'...
        messages.add_message(request, messages.ERROR, 'Não é permitido editar orçamento já finalizado.')  # noqa E501
        return redirect(reverse_lazy('orcamento:orcamento_list'))

    form = OrcamentoForm(request.POST or None, instance=orcamento_instance, prefix='main')  # noqa E501
    formset = OrcamentoItemsFormset(request.POST or None, instance=orcamento_instance, prefix='items')  # noqa E501

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('orcamento:orcamento_list')

    context = {
        'form': form,
        'formset': formset,
        'orcamento': orcamento_instance
    }
    return render(request, template_name, context)

@login_required
def orcamento_delete(request, pk):
    order_item = Orcamento.objects.get(pk=pk)
    order_item.delete()
    return redirect('orcamento:orcamento_list')


@login_required
def add_row_orcamento_items_hx(request):
    template_name = 'orcamento/hx/row_orcamento_items_hx.html'
    form = OrcamentoItensForm()
    context = {'orcamento_item_form': form}
    return render(request, template_name, context)


@login_required
def produto_preco(request):
    template_name = 'orcamento/hx/produto_preco_hx.html'
    url = request.get_full_path()
    item = url.split('-')[1]
    produto_pk = list(request.GET.values())[0]
    produto = Produto.objects.get(pk=produto_pk)

    context = {'produto': produto, 'item': item[0]}
    return render(request, template_name, context)


@login_required
def produto_items_search(request):
    template = 'orcamento/hx/orcamento_results_search.html'
    search_text = request.GET.get('search')
    results = Produto.objects.filter(titulo__icontains=search_text)
    context = {'results': results}
    return render(request, template, context)


@login_required
def orcamento_invoice(request, pk):
    template = 'orcamento/orcamento_invoice.html'
    return render(request, template)


@login_required
def contrato_create(request, orcamento_pk):
    orcamento = get_object_or_404(Orcamento, pk=orcamento_pk)
    contrato, _ = Contrato.objects.get_or_create(orcamento=orcamento)
    return redirect(reverse_lazy('orcamento:contrato_detail', kwargs={'pk': contrato.pk}))  # noqa E501


class ContratoDetailView(LRM, DetailView):
    template_name = 'contrato/contrato_detail.html'
    model = Contrato


@login_required
def clear(request):
    return HttpResponse('')


class ListEntrega(ListView,LRM):
    template_name = 'orcamento/orcamento_entrega.html'
    model = Orcamento
    context_object_name= 'entregas'
    
def orc_entrega_create(request,pk):
    template_name = 'orcamento/orcamento_entrega.html'
    entrega_instance = Orcamento.objects.get(pk=pk)

    if entrega_instance.status == 'f':
        # Se orçamento estiver 'Finalizado'...
        messages.add_message(request, messages.ERROR, 'Não é permitido editar orçamento já finalizado.')  # noqa E501
        return redirect(reverse_lazy('orcamento:orcamento_list'))

    form = EntregaForm(request.POST or None, instance=entrega_instance, prefix='main')  # noqa E501
    formset = OrcamentoItemsFormset(request.POST or None, instance=entrega_instance, prefix='items')  # noqa E501

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('orcamento:orcamento_list')

    context = {
        'form': form,
        'formset': formset,
        'orcamento': entrega_instance
    }
    return render(request, template_name, context)
