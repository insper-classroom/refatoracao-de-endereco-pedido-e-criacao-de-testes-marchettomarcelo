import pytest
from classes.Produto import Produto


@pytest.mark.produto
def test_criar_produto_id_e_nome():
    produto1 = Produto("222", "Carne")
    assert type(produto1).__name__ == "Produto"

@pytest.mark.produto
def test_criar_produto_somente_id():
    produto1 = Produto("222")
    assert type(produto1).__name__ == "Produto"
    
@pytest.mark.produto
def test_get_id_produto():
    produto1 = Produto("222")
    
    assert produto1.get_id() == "222"

@pytest.mark.produto
def test_set_id_produto():
    produto1 = Produto("222")
    produto1.set_id("111")

    assert produto1.get_id() == "111"

@pytest.mark.produto
def test_get_nome_produto():
    produto1 = Produto(nome="Carne", id_produto= "222")
    assert produto1.nome == "Carne"

@pytest.mark.produto
def test_convert_dict_produto():
    produto1 = Produto( "222", "Carne")

    assert produto1.to_dict() == {"id": "222", "nome": "Carne"}