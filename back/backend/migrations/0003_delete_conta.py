# Generated by Django 4.1 on 2022-11-24 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_cartao_validade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Conta',
        ),
    ]
