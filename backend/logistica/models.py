from django.db import models
from backend.core.models import Active, CreatedBy, DeletedBy, TimeStampedModel,Address
from backend.crm.models import Cliente
from backend.produto.models import Produto
from backend.orcamento.models import Orcamento
# Create your models here.

class Entrega(TimeStampedModel, CreatedBy, DeletedBy, Active,Address):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        related_name='entrega_orcamentos',
        null=True,
        blank=True
    )
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        related_name='orcamentos_entrega',
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        related_name='produto_orcamentos_entrega',
        null=True,
        blank=True
    )
    freteiro=models.CharField(max_length=100)
    
    class Meta:
        ordering = ('orcamento',)

    def __str__(self):
        return f'{self.orcamento}'
