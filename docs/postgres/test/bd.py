from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

""" banco (postgresql), usuário (postgres), senha (postgres), host (localhost), porta (3000) e nome do banco de dados (postgres)."""
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:3000/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
