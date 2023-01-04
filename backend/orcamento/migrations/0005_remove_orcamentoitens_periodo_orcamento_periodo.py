# Generated by Django 4.0.4 on 2022-07-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0004_alter_orcamentoitens_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orcamentoitens',
            name='periodo',
        ),
        migrations.AddField(
            model_name='orcamento',
            name='periodo',
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name='Período'),
        ),
    ]
