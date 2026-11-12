from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.orm import declarative_base,sessionmaker,Mapped,MappedColumn

Base = declarative_base()
engine = create_engine("sqlite:///files.db")

Sessinlocal = sessionmaker(engine)

class User(Base):
    __tablename__ = "Users"
    id : Mapped[int] = MappedColumn(primary_key=True)
    file_name : Mapped[str] = MappedColumn(nullable = False)
    age : Mapped[int] = MappedColumn(nullable = False)

def get_db():
    db = Sessinlocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(engine)