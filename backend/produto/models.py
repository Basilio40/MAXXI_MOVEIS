from django.db import models
from django.urls import reverse

from backend.core.models import Active, CreatedBy, DeletedBy, TimeStampedModel


class Produto(TimeStampedModel, CreatedBy, DeletedBy, Active):
    FORNECEDORES_CHOICE=[
        ('REALCE','REALCE'),
        ('RINCAO','RINCAO'),
        ('DAF','DAF'),
        ('FORMACASA','FORMACASA'),
        ('GAZIN','GAZIN'),
        ('MV','MV'),
        ('MS DECOR','MS DECOR'),
        ('ANJOS COLCHOES','ANJOS COLCHOES'),
        ('DORIGON','DORIGON'),
        ('SALA VIPP','SALA VIPP'),
        ('ZU HOUSE','ZU HOUSE'),
        ('ARTE CUBICA','ARTE CUBICA'),
        ('CRISTALFLEX','CRISTALFLEX'),
        ('MACROSUL','MACROSUL'),
        ('MAMBEL','MAMBEL'),
        ('LED','LED'),
        ('COLOMI','COLOMI'),
        ('DARCY','DARCY'),
        ('LAFF','LAFF'),
        ('ROGAR','ROGAR'),
        ('METTA MOBILI','METTA MOBILI'),
        ('MEYER','MEYER'),
        ('SALKA','SALKA'),
        ('ELEMIS','ELEMIS'),
        ('MONTE BELO','MONTE BELO'),
        ('NIRUMA','NIRUMA'),
        ('WANG E CIA','WANG E CIA'),
        ('AVOZZANI','AVOZZANI'),
        ('PREVILEGE','PREVILEGE'),
        ('SCHNEIDER','SCHNEIDER'),
        ('VITORIA DESIGNER','VITORIA DESIGNER'),

    ]
    codigo = models.CharField('Código',max_length=100)
    titulo = models.CharField('Descrição', max_length=100)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    marca = models.ForeignKey(
        'Marca',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    preco = models.DecimalField(
        'Preço_a_Vista',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )
    preco_cred = models.DecimalField(
        'Preço_a_Credito',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )
    estoque_minimo = models.PositiveIntegerField('Estoque Mínimo', null=True, blank=True)  # noqa E501
    estoque_atual = models.PositiveIntegerField('Estoque Atual', null=True, blank=True)  # noqa E501
    fabrica = models.CharField(max_length=255,choices=FORNECEDORES_CHOICE,null=True,blank=True)
    tamanho = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    tecido = models.CharField(max_length=255,blank=True,null=True)
    madeira = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.titulo}'

    def get_absolute_url(self):
        return reverse('produto:produto_detail', kwargs={'pk': self.pk})


class Patrimonio(TimeStampedModel, CreatedBy, DeletedBy, Active):
    titulo = models.CharField('Título', max_length=100, unique=True)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patrimonios',
    )

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'Patrimônio'
        verbose_name_plural = 'Patrimônios'

    def __str__(self):
        return f'{self.titulo}'


class Marca(TimeStampedModel, CreatedBy, DeletedBy, Active):
    titulo = models.CharField(max_length=100, unique=True)
    modelo = models.CharField(max_length=200)

    class Meta:
        ordering = ('titulo',)

    def __str__(self):
        return f'{self.titulo}'


class Categoria(TimeStampedModel, CreatedBy, DeletedBy, Active):
    titulo = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('titulo',)

    def __str__(self):
        return f'{self.titulo}'
