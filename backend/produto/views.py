from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import PatrimonioForm, ProdutoForm, ProdutoItemsFormset
from .models import Produto


class ProdutoListView(LRM, ListView):
    model = Produto


class ProdutoDetailView(LRM, DetailView):
    model = Produto


def produto_create(request):
    template_name = 'produto/produto_form.html'
    produto_instance = Produto()

    form = ProdutoForm(request.POST or None, instance=produto_instance, prefix='main')  # noqa E501
    formset = ProdutoItemsFormset(request.POST or None, instance=produto_instance, prefix='items')  # noqa E501

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('produto:produto_list')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)

def produto_update(request, pk):
    template_name = 'produto/produto_form.html'
    produto_instance = Produto.objects.get(pk=pk)

    form = ProdutoForm(request.POST or None, instance=produto_instance, prefix='main')  # noqa E501
    formset = ProdutoItemsFormset(request.POST or None, instance=produto_instance, prefix='items')  # noqa E501

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('produto:produto_list')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, template_name, context)

def produto_delete(request, pk):
    order_item = Produto.objects.get(pk=pk)
    order_item.delete()
    return redirect('produto:produto_list')


def add_row_produto_items_hx(request):
    template_name = 'produto/hx/row_produto_items_hx.html'
    form = PatrimonioForm()
    context = {'produto_item_form': form}
    return render(request, template_name, context)


def order_item_delete(request, pk):
    order_item = Produto.objects.get(pk=pk)
    order_item.delete()
    return HttpResponse('')


def produto_items_search(request):
    template = 'produto/hx/search-results.html'
    search_text = request.GET.get('search')
    results = Produto.objects.filter(titulo__icontains=search_text)
    context = {"results": results}
    return render(request, template, context)
