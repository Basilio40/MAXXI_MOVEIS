# Generated by Django 4.0.8 on 2022-12-28 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0019_alter_orcamento_sai_de_onde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='sai_de_onde',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='sai de onde'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='turno',
            field=models.CharField(blank=True, choices=[('COMERCIAL', 'COMERCIAL'), ('MANHÃ', 'MANHÃ'), ('TARDE', 'TARDE')], max_length=50, null=True, verbose_name='turno'),
        ),
    ]
