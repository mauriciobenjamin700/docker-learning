from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.exc import ProgrammingError

from os.path import abspath, dirname
import sys

sys.path.insert(0, dirname(abspath(__file__)))

from bd import *



class Client(Base):
    __tablename__ = "Client"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    #items = relationship("Item", back_populates="owner")

"""
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
"""

def create_entities() -> None:
    try:
        Base.metadata.create_all(engine)
        print("Tabela 'Client' criada com sucesso.")
    except ProgrammingError as e:
        print("Erro ao criar a tabela 'Client':", e)

if __name__ == "__main__":
    create_entities()