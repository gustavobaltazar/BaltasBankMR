from tabnanny import check
from django import views
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import viewsets
from rest_framework import status
from backend.models import Endereco, Usuario, Cliente, Cartao, Fatura, Transacao, Emprestimo, Favorito, Extrato
from backend.serializer import CartaoSerializer, EnderecoSerializer, UsuarioSerializer, ClienteSerializer, FaturaSerializer, TransacaoSerializer, EmprestimoSerializer, FavoritoSerializer, ExtratoSerializer, LoginSerializer, ProfileSerializer, PegaCartaoSerializer, SaldoUsuarioSerializer
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
        nome = request.data["nome"]
        senha = request.data['senha']
        tipo_conta = choice(lista_conta)
        email = request.data['email']
        senha_encriptada = make_password(senha)
        # check_senha = check_password(senha, senha_encriptada)
        saldo = 0
        data = Usuario(cpf=cpf, email=email, saldo=saldo,
                       senha=senha_encriptada, tipo_conta=tipo_conta, nome=nome)
        data.save()
        Cartao.objects.create(usuario=data)

        return Response({'detalhe': 'Usuario criado com sucesso!'}, status=status.HTTP_201_CREATED)


class UsuarioAddValueViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = SaldoUsuarioSerializer

    def create(self, request, *args, **kwargs):
        id = request.data.get('cpf')
        usuario = Usuario.objects.get(cpf=id)
        valor = request.data['saldo']

        data = Usuario(cpf=usuario, saldo=valor)
        data.save()

        usuario.saldo = float(usuario.saldo) + float(valor)
        usuario.save()

        return Response({'detalhe': 'Dinheiro adicionado com sucesso!'}, status=status.HTTP_201_CREATED)


class LoginViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = LoginSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        try:
            user = self.queryset.get(cpf=request.data['cpf'])
            if (check_password(request.data['senha'], user.senha)):
                return Response({'status': True, 'message': 'Usuario Logado!'}, status.HTTP_202_ACCEPTED)
            else:
                return Response({'status': False, 'message': 'senha incorreta'}, status.HTTP_404_NOT_FOUND)

        except:
            return Response({'status': False, 'message': 'Usuario nao existe'}, status.HTTP_404_NOT_FOUND)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        user = self.queryset.get(cpf=request.query_params.get('cpf'))
        return Response({user: user})


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
        usuario = Usuario.objects.get(cpf=id)
        numero_cartao = request.data['numero_cartao']
        cvv = request.data['cvv']
        limite = request.data['limite']
        validade = request.data['validade']
        data = Cartao(usuario=usuario, numero_cartao=numero_cartao, cvv=cvv,
                      limite=limite, validade=validade)
        data.save()
        return Response({'detalhe': 'Cartão adicionado com sucesso!'}, status=status.HTTP_201_CREATED)


class PegaCartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = PegaCartaoSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        try:
            self.queryset.get(usuario=request.data['usuario'])
            return Response(self.queryset.values().filter(usuario=request.data['usuario']), status=status.HTTP_200_OK)
        except:
            return Response({"status": False, "message": "Usuario não possui cartão registrado"}, status=status.HTTP_204_NO_CONTENT)


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
        id = request.data.get('cliente')
        transacao = request.data['transacao']
        cliente = Cliente.objects.get(id=id)
        beneficiado = Cliente.objects.get(cpf=id)
        valor_transferido = request.data['valor_transferido']

        data = Transacao(transacao=transacao, cliente=cliente, beneficiado=beneficiado,
                         valor_transferido=valor_transferido)
        data.save()

        return Response({'detalhe': 'Transacao adicionada com sucesso!'}, status=status.HTTP_201_CREATED)


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def create(self, request, *args, **kwargs):
        id = request.data.get('usuario_de')
        usuario_para_id = request.data.get('usuario_para')
        usuario_de = Usuario.objects.get(cpf=id)
        usuario_para = Usuario.objects.get(cpf=usuario_para_id)
        valor_emprestado = request.data['valor_emprestado']

        data = Emprestimo(usuario_de=usuario_de, usuario_para=usuario_para,
                          valor_emprestado=valor_emprestado)
        data.save()

        usuario_de.saldo = float(usuario_de.saldo) - float(valor_emprestado)
        usuario_de.save()
        usuario_para.saldo = float(valor_emprestado) + \
            float(usuario_para.saldo)
        usuario_para.save()

        return Response({'detalhe': 'Emprestimo adicionado com sucesso!'}, status=status.HTTP_201_CREATED)

    def __str__(self) -> str:
        return self.name


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer


class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer
