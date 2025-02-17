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
        self.validate()

    def validate(self):

        #VERIFICAR ID
        if not isinstance(self.id, UUID):
            raise Exception("id must be an UUID")

        #VERIFICAR USER_ID
        if not isinstance(self.user_id, UUID):
            raise Exception("user_id must be an UUID")

        #VERIFICAR TITULO
        if not isinstance(self.title, str) or len(self.title) == 0:
            raise Exception("title is required")

        #VERIFICAR DESCRIÇÃO
        if not isinstance(self.description, str) or len(self.description) == 0:
            raise Exception("description is required")

        #VERIFICAR STATUS
        if not isinstance(self.completed, bool) :
            raise Exception("invalid completed status: must be a boolean")
        
    def mark_as_completed(self):
        self.completed = True
