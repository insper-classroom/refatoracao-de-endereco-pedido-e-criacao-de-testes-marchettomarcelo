import pytest
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco

@pytest.mark.pessoaf
def test_Pessoa_fisica_criar_objeto_email_cps():

    pessoa1 = PessoaFisica(cpf=39409158826, email="marchetto.marcelo@gmail.com")
    assert type(pessoa1).__name__ == "PessoaFisica"


@pytest.mark.pessoaf
def test_Pessoa_fisica_criar_objeto_email_cpf_nome():
    pessoa1 = PessoaFisica(cpf=39409158826, email="marchetto.marcelo@gmail.com", nome="marcelo")
    assert type(pessoa1).__name__ == "PessoaFisica"
    

@pytest.mark.pessoaf
def test_Pessoa_fisica_adicionar_endereco():
    pessoa1 = PessoaFisica(cpf=39409158826, email="marchetto.marcelo@gmail.com", nome="marcelo")

    try:
        end1 = Endereco("04128081", "600")
        pessoa1.adicionar_endereco(apelido_endereco="casa", end=end1)
        assert False
    except:
        assert True


@pytest.mark.pessoaf
def test_Pessoa_fisica_remover_endereco():
    
    try:
        pessoa1 = PessoaFisica(cpf=39409158826, email="marchetto.marcelo@gmail.com", nome="marcelo")
        end1 = Endereco("04128081", "600")
        pessoa1.adicionar_endereco(apelido_endereco="casa", end=end1)
        pessoa1.remover_endereco("casa")
        assert True
    except:
        assert False


@pytest.mark.pessoaf
def test_Pessoa_fisica_obter_endereco():
    pessoa1 = PessoaFisica(cpf=39409158826, email="marchetto.marcelo@gmail.com", nome="marcelo")
    end1 = Endereco("04128081", "600")
    pessoa1.adicionar_endereco(apelido_endereco="casa", end=end1)

    assert pessoa1.get_endereco("casa") == end1




@pytest.mark.pessoaf
def test_Pessoa_fisica_listar_enderecos():
    pessoa1 = PessoaFisica(cpf=39409158826, email="marchetto.marcelo@gmail.com", nome="marcelo")
    
    end1 = Endereco("04128081", "600")
    end2 = Endereco("04205000", "100")

    pessoa1.adicionar_endereco(apelido_endereco="casa", end=end1)
    pessoa1.adicionar_endereco(apelido_endereco="casa2", end=end2)

    assert pessoa1.listar_enderecos() == [end1, end2]
    


def test_Pessoa_fisica_criar_objeto():
    pessoa1 = PessoaFisica(cpf=39409158826, email="marchetto.marcelo@gmail.com", nome="marcelo")
    

def test_Pessoa_fisica_criar_objeto():
    pass
def test_Pessoa_fisica_criar_objeto():
    pass