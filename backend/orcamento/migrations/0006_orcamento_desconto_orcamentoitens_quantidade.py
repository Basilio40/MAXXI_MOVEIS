# Generated by Django 4.0.4 on 2022-07-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0005_remove_orcamentoitens_periodo_orcamento_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Em porcentagem',
                                      max_digits=4, null=True, verbose_name='Desconto (%)'),
        ),
        migrations.AddField(
            model_name='orcamentoitens',
            name='quantidade',
            field=models.PositiveSmallIntegerField(
                default=1, verbose_name='Quantidade'),
        ),
    ]