# Generated by Django 4.1 on 2022-11-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_rename_data_pagamento_emprestimo_data_emprestimo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20),
            preserve_default=False,
        ),
    ]
