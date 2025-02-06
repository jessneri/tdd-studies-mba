from uuid import UUID

class User :

    id: UUID
    name: str

    def __init__(self, id:UUID, name:str):
        self.id = id
        self.name = name
        self.validade()
    
    def validade(self):
        if not isinstance(self.id, UUID):
            raise Exception("ID must be an UUID.")
        
        if not isinstance(self.name, str) or len(self.name) == 0:
            raise Exception("Name is required.")
        
    

