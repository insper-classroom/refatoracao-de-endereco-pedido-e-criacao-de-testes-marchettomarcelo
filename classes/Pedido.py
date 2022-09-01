#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
from classes.Produto import Produto

import re


class Pedido:
    EM_ABERTO = 1
    PAGO = 2

    def __init__(
            self,
            endereco_entrega: Endereco,
            endereco_faturamento: Endereco,
            pessoa: PessoaFisica,
            carrinho: Carrinho):

        self.carrinho = carrinho
        self.pessoa = pessoa
        self.endereco_entrega = endereco_entrega
        self.endereco_faturamento = endereco_faturamento
        self.status = Pedido.EM_ABERTO

    def __str__(self):
        # pessoa, endereço e produtos
        return f'Pessoa: {self.pessoa.__str__()}, Endereço de entrega: {self.endereco_entrega.__str__()}, Endereço de faturamento: {self.endereco_faturamento.__str__()}, Produtos: {self.carrinho.__str__()}'
