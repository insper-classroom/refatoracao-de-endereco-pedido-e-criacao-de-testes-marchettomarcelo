import pytest

from classes.Endereco import Endereco

def test_Endereco_erro_se_mandar_somente_cep():

    with pytest.raises(TypeError) as info:
        end1 = Endereco(cep= '01001000')
    assert "missing 1 required positional" in str(info.value)


def test_Endereco_mandando_cep_e_numero():
    
    end1 = Endereco(numero= 400, cep=18190000)
    assert type(end1).__name__ == "Endereco"
        

def test_Endereco_mandando_somente_numero():
    
    with pytest.raises(TypeError) as info:
        end1 = Endereco(numero= 400)
    assert "missing 1 required positional" in str(info.value)

    

def test_Endereco_metodo_Consultar_cep_mandando_int():
    
    end1 = Endereco.consultar_cep(cep=18190000)
    assert type(end1).__name__ == "dict"


def test_Endereco_metodo_Consultar_cep_mandando_str():
    end1 = Endereco.consultar_cep(cep="18190000")
    assert type(end1).__name__ == "dict"


def test_Endereco_metodo_Consultar_retornar_false_se_nao_for_possivel_verificar():
    end1 = Endereco.consultar_cep(00000000)
    assert end1 == False  

@pytest.mark.conect
def test_Endereco_metodo_Consultar_cep_retornar_erro_sem_conexao():
    # pytest raise errow if conection error
    with pytest.raises(Exception) as info:
        end1 = Endereco.consultar_cep("04128081")
    assert "Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known" in str(info)
    