from uuid import uuid4
from domain.task.task_entity import Task

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