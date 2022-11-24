from tabnanny import check
from django import views
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import viewsets
from rest_framework import status
from backend.models import Endereco, Usuario, Cliente, Cartao, Fatura, Transacao, Emprestimo, PagEmprestimo, Favorito, Extrato
from backend.serializer import CartaoSerializer, EnderecoSerializer, UsuarioSerializer, ClienteSerializer, FaturaSerializer, TransacaoSerializer, EmprestimoSerializer, PagEmprestimoSerializer, FavoritoSerializer, ExtratoSerializer
from rest_framework.response import Response
from random import choice


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    serializer = UsuarioSerializer(queryset, many=True)

    def create(self, request, *args, **kwargs):
        cpf = request.data['cpf']

        if len(cpf) > 11 or len(cpf) < 0:
            return Response({'detalhe': 'Número de dígitos inválido!'}, status=status.HTTP_401_UNAUTHORIZED)

        lista_conta = ['N', 'G', 'P']
        senha = request.data['senha']
        tipo_conta = choice(lista_conta)
        email = request.data['email']
        senha_encriptada = make_password(senha)
        check_senha = check_password(senha, senha_encriptada)
        data = Usuario(cpf=cpf, email=email,
                       senha=senha_encriptada, tipo_conta=tipo_conta)
        data.save()

        return Response({'detalhe': 'Usuario criado com sucesso!'}, status=status.HTTP_201_CREATED)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def create(self, request, *args, **kwargs):
        id = request.data.get('usuario')
        nome = request.data['nome']
        sobrenome = request.data['sobrenome']
        usuario = Usuario.objects.get(cpf=id)
        idade = request.data['idade']
        sexo = request.data['sexo']
        data = Cliente(nome=nome, sobrenome=sobrenome,
                       usuario=usuario, idade=idade, sexo=sexo)
        data.save()
        return Response({'detalhe': 'Cliente adicionado com sucesso!'}, status=status.HTTP_201_CREATED)


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def create(self, request, *args, **kwargs):
        id = request.data.get('cliente')
        cliente = Cliente.objects.get(id=id)
        cidade = request.data['cidade']
        bairro = request.data['bairro']
        estado = request.data['estado']
        rua = request.data['rua']
        data = Endereco(cliente=cliente, cidade=cidade,
                        estado=estado, bairro=bairro, rua=rua)
        data.save()
        return Response({'detalhe': 'Endereço adicionado com sucesso!'}, status=status.HTTP_201_CREATED)


class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

    def create(self, request, *args, **kwargs):
        id = request.data.get('usuario')
        print(id)
        usuario = Usuario.objects.get(cpf=id)
        numero_cartao = request.data['numero_cartao']
        cvv = request.data['cvv']
        limite = request.data['limite']
        validade = request.data['validade']
        data = Cartao(usuario=usuario, numero_cartao=numero_cartao, cvv=cvv,
                      limite=limite, validade=validade)
        data.save()
        return Response({'detalhe': 'Cartão adicionado com sucesso!'}, status=status.HTTP_201_CREATED)


class FaturaViewSet(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer

    def create(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id)
        valor_pago = request.data['valor_pago']
        parcelas = request.data['parcelas']
        data_pagamento = request.data['data_pagamento']
        status_pagamento = request.data['status_pagamento']

        data = Fatura(cliente=cliente, valor_pago=valor_pago, parcelas=parcelas,
                      data_pagamento=data_pagamento, status_pagamento=status_pagamento)
        data.save()

        return Response({'detalhe': 'Fatura adicionada com sucesso!'}, status=status.HTTP_201_CREATED)


class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

    def create(self, request, *args, **kwargs):
        transacao = request.data['transacao']
        cliente = Cliente.objects.get(id)
        beneficiado = Cliente.objects.get(id)
        data_transacao = request.data['data_transacao']
        valor_transferido = request.data['valor_transferido']

        data = Transacao(transacao=transacao, cliente=cliente, beneficiado=beneficiado,
                         data_transacao=data_transacao, valor_transferido=valor_transferido)
        data.save()

        return Response({'detalhe': 'Transacao adicionada com sucesso!'}, status=status.HTTP_201_CREATED)


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def create(self, request, *args, **kwargs):
        cliente_pedido = Cliente.objects.get(id)
        cliente_emprestou = Cliente.objects.get(id)
        data_pagamento = request.data['data_pagamento']
        valor_emprestado = request.data['valor_emprestado']

        data = Emprestimo(cliente_pedido=cliente_pedido, cliente_emprestou=cliente_emprestou,
                          data_pagamento=data_pagamento, valor_emprestado=valor_emprestado)

        return Response({'detalhe': 'Emprestimo adicionado com sucesso!'}, status=status.HTTP_201_CREATED)

    def __str__(self) -> str:
        return self.name


class PagEmprestimoViewSet(viewsets.ModelViewSet):
    queryset = PagEmprestimo.objects.all()
    serializer_class = PagEmprestimoSerializer

    def create(self, request, *args, **kwargs):
        emprestimo = Emprestimo.objects.get(id)
        parcelas = request.data['parcelas']
        juros = request.data['juros']
        data = PagEmprestimo(emprestimo=emprestimo,
                             parcelas=parcelas, juros=juros)
        data.save()
        return Response({'detalhe': 'Pagamento do emprestimo registrado com sucesso!'}, status=status.HTTP_201_CREATED)


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer


class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer
