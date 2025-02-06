from uuid import uuid4
from domain.user.user_entity import User
import pytest

class TestUser: 

    # TESTE PARA CONSTRUIR O USUÁRIO
    def test_user_initialization(self):
        user_id = uuid4()
        user_name = "Maria"
        user = User(id=user_id, name=user_name)

        # assert: verifica a condição e retorna um att boolean caso a condição passe
        assert user.id == user_id
        assert user.name == user_name

    # TESTE PARA VALIDAÇÃO DO ID DO USUÁRIO
    def test_user_id_validation(self):
        with pytest.raises(Exception, match="ID must be an UUID."):
            User(id="id_invalido", name="João")

    # TESTE PARA VALIDAÇÃO DO NOME DO USUÁRIO
    def test_user_name_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="Name is required."):
            User(id=user_id, name="")