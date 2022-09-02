
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