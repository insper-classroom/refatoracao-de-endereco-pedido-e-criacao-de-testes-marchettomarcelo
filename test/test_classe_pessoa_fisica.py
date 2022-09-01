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
    


@pytest.mark.pessoaf
def test_Pessoa_fisica_busca_nome():
    pessoa1 = PessoaFisica(cpf=39409158826, email="marchetto.marcelo@gmail.com", nome="marcelo")
    pessoa2 = PessoaFisica(cpf=39409158825, email="thomaz@gmail.com", nome="thomaz")
    pessoa3 = PessoaFisica(cpf=39409158824, email="arthur@gmail.com", nome="arthur")
    pessoa4 = PessoaFisica(cpf=39409158823, email="rafaels@gmail.com", nome="rafael")
    
    assert PessoaFisica.busca_nome("marcelo")[0].__str__() == "marcelo"
