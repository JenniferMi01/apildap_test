from pydantic import BaseModel

class Person(BaseModel):
    cn: str
    mail: str
    department: str