#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

# from classes.PessoaFisica import PessoaFisica
# from classes.Endereco import Endereco


# pessoa1 = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
# print(pessoa1)


# end1 = Endereco('08320330', 430)
# print(end1)

# end2 = Endereco('04546042', 300)
# print(end2)

# pessoa1.adicionar_endereco('casa', end1)

# print(pessoa1.listar_enderecos())

# pessoa1.adicionar_endereco('trabalho', end2)

# print(pessoa1.listar_enderecos())

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido

ndereco_entrega = Endereco(cep="04128081", numero=600)
enderco_faturamento = Endereco(cep="04128081", numero=600)

pessoa = PessoaFisica(cpf="12345678901", email="marchetto.marcelo@gmail.com")
carrinho = Carrinho()

pedido1 = Pedido(endereco_entrega=pessoa, endereco_faturamento=enderco_faturamento, pessoa=pessoa, carrinho=carrinho)

print(pedido1)