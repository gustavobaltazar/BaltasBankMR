from django.contrib import admin

from .models import Cartao, Cliente, Emprestimo, Endereco, Extrato, Fatura, Favorito, PagEmprestimo, Usuario, Transacao

class UsuarioLista(admin.ModelAdmin):
    model = Usuario
    list_display = ['cpf', 'tipo_conta']

admin.site.register(Usuario, UsuarioLista)

class ClienteLista(admin.ModelAdmin):
    model = Cliente
    list_display = ['nome', 'sobrenome', 'idade']

admin.site.register(Cliente, ClienteLista)


class CartaoLista(admin.ModelAdmin):
    model = Cartao
    list_display = ['numero_cartao', 'validade']

admin.site.register(Cartao, CartaoLista)

class EnderecoLista(admin.ModelAdmin):
    model = Endereco
    list_display = ['cliente', 'cidade', 'bairro']
admin.site.register(Endereco, EnderecoLista)

class FaturaLista(admin.ModelAdmin):
    model = Fatura
    list_display = ['cliente', 'parcelas', 'data_pagamento', 'status_pagamento']
admin.site.register(Fatura, FaturaLista)

class TransacaoLista(admin.ModelAdmin):
    model = Transacao
    list_display = ['cliente', 'beneficiado', 'transacao']
admin.site.register(Transacao, TransacaoLista)

class EmprestimoLista(admin.ModelAdmin):
    model = Emprestimo
    list_display = ['cliente_de', 'cliente_para', 'valor_emprestado']
admin.site.register(Emprestimo, EmprestimoLista)

class PagEmprestimoLista(admin.ModelAdmin):
    model = PagEmprestimo
    list_display = ['emprestimo','parcelas', 'juros']
admin.site.register(PagEmprestimo, PagEmprestimoLista)

class FavoritoLista(admin.ModelAdmin):
    model = Favorito
    list_display = ['cliente_favoritado']
admin.site.register(Favorito, FavoritoLista)

class ExtratoLista(admin.ModelAdmin):
    model = Extrato
    list_display = ['emprestimo_feito', 'transacao_feita', 'fatura_obtida']
admin.site.register(Extrato, ExtratoLista)
