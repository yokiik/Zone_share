from pydantic import BaseModel

class Base(BaseModel):
    pass

class UserCreate(Base):
    login: str
    password: str

class UserAuthorization(Base):
    login: str
    password: str

class UserRead(Base):
    id: int
    login : str