
import pytest

from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto

#  ---------- Testes que substituem o main3.py  ----------
@pytest.mark.main3
def test_main3_cria_pessoa_e_adiciona_dois_enderecos_e_lista_enderecos():

    pessoa1 = PessoaFisica(nome= 'Carlos', email='tiago@email.com', cpf ='524.222.452-6')
    
    # Cria  um endereço
    end1 = Endereco(cep='08320330', numero= 430)

    # Cria um outro endereço
    end2 = Endereco(cep='04546042', numero=300)
    
    # Adiciona endereço à pessoa
    pessoa1.adicionar_endereco(apelido_endereco='casa', end=end1)

    
    um_endereco = pessoa1.listar_enderecos()
    assert um_endereco == [end1]

    pessoa1.adicionar_endereco('trabalho', end2)
    
    dois_enderecos = pessoa1.listar_enderecos()
    assert dois_enderecos == [end1, end2]

@pytest.mark.main3
def test_main3_cria_produto():

    sabonete = Produto(id_produto="0010342967", nome="Sabonete")
    assert sabonete.get_id() == "0010342967"
    assert sabonete.nome == "Sabonete"


@pytest.mark.main3
def test_main3_selecionando_pessoa_com_busca_nome():    
    pessoa1 = PessoaFisica(nome= 'Tom', email='tiago@email.com', cpf ='524.222.452-6')    
    pessoas_escolhidas = PessoaFisica.busca_nome('Tom')

    if len(pessoas_escolhidas) > 0: 
        pessoa_escolhida = pessoas_escolhidas[0]  #Pega a primeira pessoa_escolhida
    
    assert pessoa_escolhida == pessoa1


@pytest.mark.main3
def test_main3_selecionando_pessoa_com_busca_nome_invalido():    
    pessoa_falsa = PessoaFisica(nome= 'Putim', email='putim@email.com', cpf ='524.222.452-6')    


    pessoa1 = PessoaFisica(nome= 'Tomy', email='tomy@email.com', cpf ='524.222.452-6')    
    pessoa2 = PessoaFisica(nome= 'Ymot', email='ymot@email.com', cpf ='524.222.452-6')    
    
    pessoas_com_nome_x = PessoaFisica.busca_nome('Tom')

    pessoa_escolhida = []

    if len(pessoas_com_nome_x) > 0: 
        pessoa_escolhida = pessoas_com_nome_x[0]  #Pega a primeira pessoa_escolhida
    

    assert pessoa_escolhida != pessoa_falsa



@pytest.mark.main3
def test_main3_selecionando_produtos_com_busca_nome():    
    
    limao = Produto(id_produto="0010342967", nome="limao")
    
    produtos_selecionados = Produto.busca_nome("limao")

    if len(produtos_selecionados) > 0: 
        produto = produtos_selecionados[0]
    
    assert produto == limao





@pytest.mark.main3
def test_main3_selecionando_produtos_com_busca_nome_invalido():    
    
    limao = Produto(id_produto="0010342967", nome="limao")
    laranja = Produto(id_produto="0010342967", nome="laranja")
    
    produtos_selecionados = Produto.busca_nome("limao")

    if len(produtos_selecionados) > 0: 
        produto = produtos_selecionados[0]
    
    assert produto != laranja

@pytest.mark.main3
def test_main3_criando_carrinho_e_adiciona_produto():    
    
    batata = Produto(id_produto="00103442437", nome="batata")
    pessoa = PessoaFisica(nome= 'Tiago', email="tiago.gmail.com", cpf="524.222.452-6")
    
    endereco_entrega = Endereco(cep='04546042', numero=300)
    endereco_faturamento = Endereco(cep='04546044', numero=300)

    carrinho = Carrinho()
    carrinho.adicionar_item(batata, 10)

    pedido = Pedido(carrinho=carrinho, pessoa=pessoa, endereco_entrega=endereco_entrega, endereco_faturamento=endereco_faturamento)

    assert pedido.carrinho == carrinho
    assert pedido.pessoa == pessoa
    assert pedido.endereco_entrega == endereco_entrega
    assert pedido.endereco_faturamento == endereco_faturamento
    
      



@pytest.mark.main3
def test_main3_cria_pessoas_e_lista_enderecos():    
    
    pessoa = PessoaFisica(nome= 'Tiago', email="tiago.gmail.com", cpf="524.222.452-6")
    
    endereco_entrega = Endereco(cep='04546042', numero=300)
    endereco_faturamento = Endereco(cep='04546044', numero=300)

    pessoa.adicionar_endereco("entrega",endereco_entrega)
    pessoa.adicionar_endereco("faturamento",endereco_faturamento)

    ends = pessoa.listar_enderecos()


    assert ends[0] == endereco_entrega


@pytest.mark.main3
def test_main3_cria_pedido_e_processa_pagamento():   
    endereco_entrega = Endereco(cep="04128081", numero=600)
    enderco_faturamento = Endereco(cep="04128081", numero=600)

    pessoa = PessoaFisica(cpf="12345678901", email="marchetto.marcelo@gmail.com")
    carrinho = Carrinho()

    pedido = Pedido(endereco_entrega=endereco_entrega, endereco_faturamento=enderco_faturamento, pessoa=pessoa, carrinho=carrinho)

    pag = Pagamento(pedido)
    pag.processa_pagamento()
    if pag.pagamento_aprovado:
        pedido.status = Pedido.PAGO 
    
    assert pedido.status == Pedido.PAGO