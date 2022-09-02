#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento


import copy

# Caso de uso em que se busca uma pessoa e um produto
# Cria uma pessoa 
pessoa1 = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
print(pessoa1)

# Cria  um endereço
end1 = Endereco('08320330', 430)
print(end1)

# Cria um outro endereço
end2 = Endereco('04546042', 300)
print(end2)

# Adiciona endereço à pessoa
pessoa1.adicionar_endereco('casa', end1)

print("Endereços da pessoa")
print(pessoa1.listar_enderecos())

pessoa1.adicionar_endereco('trabalho', end2)
print("Endereços da pessoa após inclusão")
print(pessoa1.listar_enderecos())

# Criando um produto
sabonete = Produto(id_produto="0010342967", nome="Sabonete")

##############################################
# Fim do setup
###########################################

pessoas = PessoaFisica.busca_nome('Carlos')
if len(pessoas) > 0:
    pessoa = pessoas[0]  #Pega a primeira pessoa


produtos = Produto.busca_nome("Sabonete")

if len(produtos) > 0: 
    produto = produtos[0]


carrinho = Carrinho()
carrinho.adicionar_item(sabonete, 10)

pedido = Pedido(carrinho=carrinho, pessoa=pessoa1, endereco_entrega=end1, endereco_faturamento=end2)

ends = pessoa1.listar_enderecos()

if len(ends) > 0:
    endereco = ends[0]

# Lembre-se de adicionar estes atributos ao endereço
pedido.endereco_entrega = copy.deepcopy(endereco) 
pedido.endereco_faturamento = copy.deepcopy(endereco)


pag = Pagamento(pedido)
pag.processa_pagamento()
if pag.pagamento_aprovado:
    pedido.status = Pedido.PAGO 

print("Pedido aguardando coleta")

## Pedido deve imprir todos os detalhes da compra - pessoa, endereço e produtos
print(pedido)



