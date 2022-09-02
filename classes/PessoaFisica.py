#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.

    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    lista_pessoas_fisicas = []

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.lista_pessoas_fisicas.append(self)

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end: Endereco):
        self.__enderecos[apelido_endereco] =  end

    def remover_endereco(self, apelido_endereco):
        del self.__enderecos[apelido_endereco]

    def get_endereco(self, apelido_endereco):
        return self.__enderecos[apelido_endereco]

    def listar_enderecos(self):
        return list(self.__enderecos.values())

    def busca_nome(nome_sendo_buscado):
        pessoas_com_nome_sendo_buscado = []

        for i in PessoaFisica.lista_pessoas_fisicas:

            if i.nome == nome_sendo_buscado:
                pessoas_com_nome_sendo_buscado.append(i)

        print(pessoas_com_nome_sendo_buscado)
        return pessoas_com_nome_sendo_buscado

    def __str__(self):
        return str(self.nome)
