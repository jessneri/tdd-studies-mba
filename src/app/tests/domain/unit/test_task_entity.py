from uuid import uuid4
from domain.task.task_entity import Task
import pytest

class TestTask:

    # TESTE PARAVERIFICAR O CONSTRUTOR DA TAREFA
    def test_task_initialization(self):

        task_id = uuid4()
        user_id = uuid4()
        title = "Estudar testes."
        description = "Os testes unitários são os mais baratos."
        completed = False

        task = Task(
            id=task_id,
            user_id=user_id,
            title=title,
            description=description,
            completed=completed
        )

        assert task.id == task_id
        assert task.user_id == user_id
        assert task.title == title
        assert task.description == description
        assert task.completed == completed

    # TESTE PRA VALIDAÇÃO DO ID DA TAREFA
    def test_task_id_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="id must be an UUID"):
            Task(
                id="not_uuid",
                user_id=user_id,
                title="Título",
                description="Descrição da tarefa",
                completed=False
            )

    # TESTE PARA VERIFICAR O ID DO USUÁRIO
    def test_taks_user_id_validation(self):
        task_id = uuid4()
        with pytest.raises(Exception, match="user_id must be an UUID"):
            Task(
                id=task_id,
                user_id="not_uuid",
                title="Título",
                description="Descrição da tarefa",
                completed=False
            )

    # TESTE PARA VERIFICAR A VALIDAÇÃO DO TITULO
    def test_taks_title_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="title is required"):
            Task(
                id=task_id,
                user_id=user_id,
                title="",
                description="Descrição da tarefa",
                completed=False
            )

    # TESTE PARA VERIFICAR A VALIDAÇÃO DA DESCRIÇÃO
    def test_taks_description_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="description is required"):
            Task(
                id=task_id,
                user_id=user_id,
                title="Título",
                description="",
                completed=False
            )

    # TESTE PARA VERIFICAR A VALIDAÇÃO DO STATUS "COMPLETED" DA TAREFA
    def test_taks_completed_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="invalid completed status: must be a boolean"):
            Task(
                id=task_id,
                user_id=user_id,
                title="Título",
                description="Descrição da tarefa",
                completed="not_boolean"
            )

    # TESTE PARA VERIFICAR SE UMA TAREFA FOI COMPLETADA COM UMA FUNÇÃO mark_as_completed
    def test_mark_as_completed(self):
        # instanciar a minha classe Task 
        task = Task(
                id=uuid4(),
                user_id=uuid4(),
                title="Título",
                description="Descrição da tarefa",
                completed=False
            )
        
        # marcar a tarefa como concluída
        task.mark_as_completed()

        # verificar se o atributo foi atualizado para True
        assert task.completed == True

