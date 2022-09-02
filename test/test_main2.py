from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import copy

import pytest

#  ---------- Testes que substituem o main2.py  ----------
@pytest.mark.main2
def test_main2_cria_pessoa_e_adiciona_dois_enderecos_e_lista_enderecos():
    pessoa1 = PessoaFisica(cpf=39409158825, email="marchetto.marcelo@gmail.com")
    
    endereco_casa = Endereco("04128081", "600")
    endereco_trabalho = Endereco("04128081", "601")
    
    pessoa1.adicionar_endereco(apelido_endereco="casa", end=endereco_casa)
    pessoa1.adicionar_endereco(apelido_endereco="trabalho", end=endereco_trabalho)

    assert pessoa1.listar_enderecos() == [endereco_casa, endereco_trabalho]

@pytest.mark.main2
def test_main2_produto_cria_carrinho_e_adiciona_o_produto_nele():
    
    sabonete = Produto(id_produto="0010342967", nome="Sabonete")
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete, 5)
    
    assert carrinho.itens == {"0010342967": 5}

@pytest.mark.main2
def test_main2_cria_pedido():
    pessoa = PessoaFisica(cpf="12345678901", email="marcelovfm@al.inpser.edu.br")
    endereco_entrega = Endereco(cep="04128081", numero=600)
    endereco_faturamento = Endereco(cep="04128081", numero=600)
    carrinho = Carrinho()
    pedido = Pedido(endereco_entrega=endereco_entrega, endereco_faturamento=endereco_faturamento, pessoa=pessoa, carrinho=carrinho)

    assert pedido.endereco_entrega == endereco_entrega
    assert pedido.endereco_faturamento == endereco_faturamento
    assert pedido.pessoa == pessoa
    assert pedido.carrinho == carrinho
    assert type(pedido) == Pedido


@pytest.mark.main2
def test_main2_cria_pedido_e_processa_pagamento():
    pessoa = PessoaFisica(cpf="12345678901", email="marcelo@gmail.com")
    endereco_entrega = Endereco(cep="04128081", numero=600)
    endereco_faturamento = Endereco(cep="04128081", numero=600)
    
    carrinho = Carrinho()
    pedido = Pedido(endereco_entrega=endereco_entrega, endereco_faturamento=endereco_faturamento, pessoa=pessoa, carrinho=carrinho)
    pagamento = Pagamento(pedido=pedido)
    pagamento.processa_pagamento()

    assert pagamento.pagamento_aprovado == True
    assert pagamento.pedido == pedido
    assert pedido.status == Pedido.PAGO

# ---------- Testes extras ----------
@pytest.mark.main2
def test_main2_cria_pagamenteo_sem_pedido():
    pessoa = PessoaFisica(cpf="12345678901", email="marcelo@gmail.com")
    endereco_entrega = Endereco(cep="04128081", numero=600)
    endereco_faturamento = Endereco(cep="04128081", numero=600)
    
    carrinho = Carrinho()
    pedido = Pedido(endereco_entrega=endereco_entrega, endereco_faturamento=endereco_faturamento, pessoa=pessoa, carrinho=carrinho)
    
    with pytest.raises(TypeError):
        pagamento = Pagamento()
    
@pytest.mark.main2
def test_main2_cria_pessoa_e_adiciona_dois_enderecos_e_lista_enderecos():
    pessoa1 = PessoaFisica(cpf=39409158825, email="marchetto.marcelo@gmail.com")
    
    endereco_casa = Endereco("04128081", "600")
    endereco_trabalho = Endereco("04128081", "601")
    
    pessoa1.adicionar_endereco(apelido_endereco="casa", end=endereco_casa)
    pessoa1.adicionar_endereco(apelido_endereco="trabalho", end=endereco_trabalho)

    assert pessoa1.listar_enderecos() == [endereco_casa, endereco_trabalho]    

