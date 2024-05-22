# Função para adicionar um registro à tabela Client
from sqlalchemy.exc import IntegrityError

from os.path import abspath, dirname
import sys

sys.path.insert(0, dirname(abspath(__file__)))

from bd import SessionLocal
from entities import Client

def add_client(email, hashed_password, is_active=True):
    # Criando a sessão

    session = SessionLocal()
    
    try:
        client = Client(email=email, hashed_password=hashed_password, is_active=is_active)
        session.add(client)
        session.commit()
        print("Registro adicionado com sucesso.")
    except IntegrityError:
        session.rollback()
        print("Erro: Já existe um registro com o email fornecido.")
    finally:
        session.close()

if __name__ == "__main__":
    # Função para inserir 5 registros de exemplo
    def insert_example_clients():
        for i in range(1, 6):
            email = f"client{i}@example.com"
            hashed_password = f"password{i}"
            add_client(email, hashed_password)

    # Inserindo 5 registros de exemplo
    insert_example_clients()