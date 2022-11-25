# Generated by Django 4.1 on 2022-11-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_usuario_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='saldo',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20),
            preserve_default=False,
        ),
    ]
