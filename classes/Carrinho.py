#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica


# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item


class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.__itens = {}

    @property
    def itens(self):
        return self.__itens

    def adicionar_item(self, item: Produto, qtd):
        if qtd <= 0:
            raise ValueError('Quantidade deve ser maior que 0')

        id_item = item.get_id()

        self.__itens[id_item] = qtd
        # Implemente a adição do item no dicionário

    def remover_item(self, item: Produto):
        id_item = item.get_id()
        if id_item in self.__itens:
            del self.__itens[id_item]
        else:
            raise ValueError('Item não encontrado no carrinho')
    


    def __str__(self):

        return f'{self.__itens}'

