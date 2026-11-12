from sqlalchemy import create_engine,String,Integer,Column,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,Mapped,MappedColumn

Base = declarative_base()
engine = create_engine("sqlite:///files.db")

Sessinlocal = sessionmaker(engine)

class User(Base):
    __tablename__ = "Users"
    id : Mapped[int] = MappedColumn(primary_key=True)
    name : Mapped[str] = MappedColumn(nullable = False)

class File(Base):
    __tablename__ = "File"
    id : Mapped[int] = MappedColumn(primary_key=True)
    filename : Mapped[str] = MappedColumn(nullable = False)
    filetype : Mapped[str] = MappedColumn(nullable = False)
    ownerid : Mapped[int] = MappedColumn(ForeignKey = "Users.id")

def get_db():
    db = Sessinlocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(engine)