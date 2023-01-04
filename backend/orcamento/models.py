from datetime import timedelta

from django.db import models
from django.urls import reverse_lazy

from backend.core.models import Active, CreatedBy, DeletedBy, TimeStampedModel,Address
from backend.crm.models import Cliente
from backend.produto.models import Patrimonio, Produto

STATUS_ORCAMENTO = (
    ('p', 'Pendente'),
    ('f', 'Finalizado'),
    ('c', 'Cancelado'),
)



class Orcamento(TimeStampedModel, CreatedBy, DeletedBy, Active,Address):
    CNPJ = 'CNPJ'
    CPF = 'CPF'

    TIPO_REGISTRO = [
        (CNPJ, CNPJ),
        (CPF, CPF),
    ]
    FRETE_CHOICE=[
        ('isento','ISENTO'),
        ('cobrado','COBRADO'),
        ('retira','RETiRA')
    ]
    
    MONTAGEM_CHOICE =[
        ('sim','SIM'),
        ('não','NÃO')
    ]
    
    IMPERMEAB_CHOICE =[
        ('sim','SIM'),
        ('não','NÃO')
    ]
    
    TURNO_CHOICE = [
        ('COMERCIAL','COMERCIAL'),
        ('MANHÃ','MANHÃ'),
        ('TARDE','TARDE')
    ]
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        related_name='cliente_orcamentos',
        null=True,
        blank=True
    )
    periodo = models.PositiveSmallIntegerField('Período (em dias)', default=0)
    desconto = models.DecimalField(
        'Desconto (%)',
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Em porcentagem'
    )
    status = models.CharField(max_length=1, choices=STATUS_ORCAMENTO, default='p')  # noqa E501
    tipo = models.CharField(max_length=4, choices=TIPO_REGISTRO, default=CNPJ)
    rg = models.CharField('RG', max_length=20, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=14, null=True, blank=True)
    inscricao_est = models.CharField('Inscrição Estadual', max_length=250, null=True, blank=True)  # noqa E501
    frete = models.CharField(max_length=30,choices=FRETE_CHOICE)
    montagem = models.CharField(max_length=30,choices=MONTAGEM_CHOICE,null=True,blank=True)
    endereco_entrega = models.CharField('Endereço Entrega', max_length=250, null=True, blank=True)
    freteiro = models.CharField('freteiro', max_length=150,null=True, blank=True)
    impermmeab = models.CharField(max_length=30,choices=IMPERMEAB_CHOICE,null=True,blank=True)
    data_entrega = models.DateTimeField('data de entrega', auto_now_add=False,null=True,blank=True)
    sai_de_onde = models.CharField('sai de onde', max_length=255,null=True,blank=True)
    turno = models.CharField('turno',max_length=50,choices=TURNO_CHOICE,null=True,blank=True)
    loja = models.CharField('Loja n°',max_length=20,null=True,blank=True)
    obs_vendas = models.CharField('Observações', max_length=500, null=True,blank=True)
    obs_interna = models.CharField(max_length=500,null=True,blank=True)
    

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'

    def __str__(self):
        return f'{str(self.pk).zfill(3)}'

    def get_absolute_url(self):
        return reverse_lazy('orcamento:orcamento_detail', kwargs={'pk': self.pk})

    def total(self):
        qs = self.orcamentos.filter(orcamento=self.pk).values_list(
            'valor', 'quantidade') or 0
        total = 0 if isinstance(qs, int) else sum(
            map(lambda q: q[0] * q[1], qs))
        return total


class OrcamentoItens(models.Model):
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        related_name='orcamentos',
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        related_name='produto_orcamentos',
        null=True,
        blank=True
    )
    patrimonio = models.ForeignKey(
        Patrimonio,
        on_delete=models.SET_NULL,
        related_name='patrimonio_orcamentos',
        null=True,
        blank=True
    )
    quantidade = models.PositiveSmallIntegerField('Quantidade', default=1)
    valor = models.DecimalField(
        'Valor',
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Orçamento Item'
        verbose_name_plural = 'Orçamento Itens'

    def __str__(self):
        return f'{self.pk}'

    def subtotal(self):
        return self.valor * (self.quantidade or 0)


STATUS_CONTRATO = (
    ('p', 'Pendente'),
    ('f', 'Finalizado'),
    ('c', 'Cancelado'),
)


class Contrato(TimeStampedModel, CreatedBy, DeletedBy, Active):
    orcamento = models.OneToOneField(
        Orcamento,
        verbose_name='orçamento',
        related_name='contrato',
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=1, choices=STATUS_CONTRATO, default='p')  # noqa E501

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'contrato'
        verbose_name_plural = 'contratos'

    @property
    def codigo(self):
        return str(self.pk).zfill(3)

    def __str__(self):
        return f'{self.codigo}'

    @property
    def data_final(self):
        return self.created + timedelta(self.orcamento.periodo)

    def get_absolute_url(self):
        return reverse_lazy('orcamento:contrato_detail', pk=self.pk)
