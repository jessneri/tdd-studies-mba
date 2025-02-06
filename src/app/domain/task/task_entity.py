from uuid import UUID


class Task:

    id: UUID
    user_id: UUID
    title: str
    description: str
    completed: bool

    def __init__(
        self, id: UUID, user_id: UUID, title: str, description: str, completed: bool
    ):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.completed = completed
