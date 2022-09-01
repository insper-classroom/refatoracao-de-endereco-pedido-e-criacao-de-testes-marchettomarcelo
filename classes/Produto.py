#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    lista_produtos = []

    def __init__(self, id_produto, nome=''):
        self.__id = id_produto
        self.__nome = nome
        Produto.lista_produtos.append(self)

    def set_id(self, id_produto):
        self.__id = id_produto

    def get_id(self):
        return self.__id

    @classmethod
    def busca_nome(cls, produto_sendo_buscado):
        produtos_com_nome_sendo_buscado = []

        for i in cls.lista_produtos:

            if i.nome == produto_sendo_buscado:
                produtos_com_nome_sendo_buscado.append(i)

        return produtos_com_nome_sendo_buscado

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nove_nome):
        if nove_nome[0] != 'T':
            self.__nome = nove_nome

    def to_dict(self):
        return {"id": self.__id, "nome": self.nome}
