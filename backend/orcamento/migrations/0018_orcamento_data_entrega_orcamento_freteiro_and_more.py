# Generated by Django 4.0.8 on 2022-12-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0017_orcamento_frete_orcamento_montagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='data_entrega',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data de entrega'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='freteiro',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='freteiro'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='impermmeab',
            field=models.CharField(blank=True, choices=[('sim', 'SIM'), ('não', 'NÃO')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='loja',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Loja n°'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='obs_interna',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='obs_vendas',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Observações'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='sai_de_onde',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='sai de onde'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='turno',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='turno'),
        ),
    ]
