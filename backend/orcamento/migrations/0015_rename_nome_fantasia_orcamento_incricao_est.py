# Generated by Django 4.0.8 on 2022-12-11 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0014_orcamento_cnpj_orcamento_cpf_orcamento_nome_fantasia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orcamento',
            old_name='nome_fantasia',
            new_name='incricao_est',
        ),
    ]
