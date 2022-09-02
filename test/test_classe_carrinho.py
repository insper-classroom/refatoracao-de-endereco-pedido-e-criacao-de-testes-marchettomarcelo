import pytest

from classes.Produto import Produto
from classes.Carrinho import Carrinho

@pytest.mark.carrinho
def test_Carrinho_criar_carrinho():
    carrinho1 = Carrinho()
    assert type(carrinho1).__name__ == "Carrinho"

@pytest.mark.carrinho
def test_Carrinho_adicionar_coisas_carrinho():
    
    
    produto1 = Produto("222", "Carne")
    carrinho1 = Carrinho()
    carrinho1.adicionar_item(produto1, 2)
    id_produto1 = produto1.get_id()
    
    assert carrinho1.itens == {id_produto1: 2}

@pytest.mark.carrinho
def test_Carrinho_adicionar_quantidade_negativa_carrinho():

    # retorna False se adicinar quantidade negativa
    with pytest.raises(ValueError):
        produto1 = Produto("222", "Carne")
        carrinho1 = Carrinho()
        carrinho1.adicionar_item(produto1, -2)
    

@pytest.mark.carrinho
def test_Carrinho_remover_coisas_carrinho():
    
    
    produto1 = Produto("222", "Carne")
    carrinho1 = Carrinho()

    carrinho1.adicionar_item(produto1, 2)
    carrinho1.remover_item(produto1)
    
    assert carrinho1.itens == {}

@pytest.mark.carrinho
def test_Carrinho_remover_coisas_carrinho():
 
    produto1 = Produto("222", "Carne")
    
    carrinho1 = Carrinho()
    carrinho1.adicionar_item(produto1, 2)
    carrinho1.remover_item(produto1)
    
    assert carrinho1.itens == {}
    
@pytest.mark.carrinho
def test_Carrinho_remover_coisas_nao_adicionadas_carrinho():
    
    
    produto1 = Produto("222", "Carne")
    produto2 = Produto("2", "Arroz")
    carrinho1 = Carrinho()

    # check value error
    with pytest.raises(ValueError):
        carrinho1.adicionar_item(produto1, 2)
        carrinho1.remover_item(produto2)