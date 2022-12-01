from random import choices
from django.db import models
from random import randint


class Usuario(models.Model):
    NORMAL = 'N'
    GOLD = 'G'
    PLATINUM = 'P'

    TIPOS_CONTA = [
        (NORMAL, 'Normal'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
    ]
    cpf = models.CharField(primary_key=True, max_length=15)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    tipo_conta = models.CharField(max_length=1, choices=TIPOS_CONTA)
    saldo = models.DecimalField(max_digits=20, decimal_places=2, blank=True)

    def __str__(self) -> str:
        return self.cpf


class Cartao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    numero_cartao = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    limite = models.DecimalField(max_digits=20, decimal_places=6)
    validade = models.CharField(max_length=6)

    def save(self, *args, **kwargs):
        self.numero_cartao = f"{randint(1000, 9999)} {randint(1000, 9999)} {randint(1000, 9999)} {randint(1000, 9999)}"
        self.cvv = f"{randint(100, 999)}"
        self.validade = f"{randint(1,12)}/{randint(30,35)}"
        if self.usuario.tipo_conta == "N":
            self.limite = float(randint(400, 2000))
        elif self.usuario.tipo_conta == "G":
            self.limite = float(randint(2000, 4500))
        else:
            self.limite = float(randint(4500, 10000))
        super(Cartao, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.numero_cartao


class Cliente(models.Model):
    SEXO_MASCULINO = 'M'
    SEXO_FEMININO = 'F'
    SEXO_INDEFINIDO = '?'

    SEXO_TIPOS = [
        (SEXO_MASCULINO, 'Male'),
        (SEXO_FEMININO, 'Female'),
        (SEXO_INDEFINIDO, '?'),
    ]

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_TIPOS)

    def __str__(self) -> str:
        return self.nome


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.cidade


class Fatura(models.Model):
    STATUS_PAGO = 'P'
    STATUS_NAO_PAGO = 'NP'

    STATUS_PAGAMENTO = [
        (STATUS_PAGO, 'P'),
        (STATUS_NAO_PAGO, 'NP'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=20, decimal_places=2)
    parcelas = models.IntegerField()
    status_pagamento = models.CharField(max_length=2, choices=STATUS_PAGAMENTO)

    list_display = [cliente, parcelas, status_pagamento]

    def __str__(self) -> str:
        return str(self.valor_pago)


class Transacao(models.Model):
    TED = 'TE'
    DOC = 'DO'
    BOLETO = 'BO'
    VOUCHER = 'VO'
    DUPLICATAS = 'DU'

    TIPO_TRANSACAO = [
        (TED, 'TE'),
        (DOC, 'DO'),
        (BOLETO, 'BO'),
        (VOUCHER, 'VO'),
        (DUPLICATAS, 'DU'),
    ]

    transacao = models.CharField(max_length=2, choices=TIPO_TRANSACAO)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, related_name='cliente')
    beneficiado = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, related_name='beneficiado')
    valor_transferido = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return self.transacao


class Emprestimo(models.Model):
    usuario_de = models.ForeignKey(
        Usuario, on_delete=models.DO_NOTHING, related_name='usuario_de')
    usuario_para = models.ForeignKey(
        Usuario, on_delete=models.DO_NOTHING, related_name='usuario_para')
    valor_emprestado = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return str(self.cliente_de)


class Favorito(models.Model):
    possui_favorito = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, related_name="possui_favorito")
    cliente_favoritado = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, related_name="cliente_favoritado")


class Extrato(models.Model):
    emprestimo_feito = models.ForeignKey(
        Emprestimo, on_delete=models.DO_NOTHING)
    transacao_feita = models.ForeignKey(Transacao, on_delete=models.DO_NOTHING)
    fatura_obtida = models.ForeignKey(Fatura, on_delete=models.DO_NOTHING)
