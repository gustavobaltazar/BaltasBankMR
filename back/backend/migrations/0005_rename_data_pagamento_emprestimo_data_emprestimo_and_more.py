# Generated by Django 4.1 on 2022-11-25 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_cliente_pedido_emprestimo_cliente_de_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo',
            old_name='data_pagamento',
            new_name='data_emprestimo',
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='cliente_de',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente_de', to='backend.cliente'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='cliente_para',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente_para', to='backend.cliente'),
        ),
    ]