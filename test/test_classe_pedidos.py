import pytest

from classes.Pedido import Pedido
from classes.Carrinho import Carrinho
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco


@pytest.mark.pedido
def test_Pedido_criar_pedido():
    endereco_entrega = Endereco(cep="04128081", numero=600)
    enderco_faturamento = Endereco(cep="04128081", numero=600)

    pessoa = PessoaFisica(cpf="12345678901", email="marchetto.marcelo@gmail.com")
    carrinho = Carrinho()

    pedido1 = Pedido(endereco_entrega=endereco_entrega, endereco_faturamento=enderco_faturamento, pessoa=pessoa, carrinho=carrinho)

    assert type(pedido1).__name__ == "Pedido"

@pytest.mark.pedido
def test_Pedido_criar_pedido_sem_endereco_entrega():
    
    enderco_faturamento = Endereco(cep="04128081", numero=600)

    pessoa = PessoaFisica(cpf="12345678901", email="marchetto.marcelo@gmail.com")
    carrinho = Carrinho()

    # check if ValueError is raised
    with pytest.raises(TypeError):
        pedido1 = Pedido(endereco_faturamento=enderco_faturamento, pessoa=pessoa, carrinho=carrinho)


@pytest.mark.pedido
def test_Pedido_criar_pedido_sem_endereco_faturamento():
    endereco_entrega = Endereco(cep="04128081", numero=600)

    pessoa = PessoaFisica(cpf="12345678901", email="marchetto.marcelo@gmail.com")
    carrinho = Carrinho()

    # check if ValueError is raised
    with pytest.raises(TypeError):
        pedido1 = Pedido(endereco_entrega=endereco_entrega, pessoa=pessoa, carrinho=carrinho)


@pytest.mark.pedido
def test_Pedido_criar_pedido_sem_pessoa():
    
    endereco_entrega = Endereco(cep="04128081", numero=600)
    enderco_faturamento = Endereco(cep="04128081", numero=600)

    carrinho = Carrinho()
    # check if ValueError is raised
    with pytest.raises(TypeError):
        pedido1 = Pedido(endereco_entrega=endereco_entrega, endereco_faturamento=enderco_faturamento,carrinho=carrinho)

@pytest.mark.pedido
def test_Pedido_criar_pedido_sem_carrinho():
    
    endereco_entrega = Endereco(cep="04128081", numero=600)
    enderco_faturamento = Endereco(cep="04128081", numero=600)

    pessoa = PessoaFisica(cpf="12345678901", email="marchetto.marcelo@gmail.com")
    
    # check if ValueError is raised
    with pytest.raises(TypeError):
        pedido1 = Pedido(endereco_entrega=endereco_entrega, endereco_faturamento=enderco_faturamento, pessoa=pessoa)


@pytest.mark.pedido
def test_Pedido_criar_pedido_sem_pessoa():
    
    endereco_entrega = Endereco(cep="04128081", numero=600)
    enderco_faturamento = Endereco(cep="04128081", numero=600)

    
    carrinho = Carrinho()
    # check if ValueError is raised
    with pytest.raises(TypeError):
        pedido1 = Pedido(endereco_entrega=endereco_entrega, endereco_faturamento=enderco_faturamento, carrinho=carrinho)
