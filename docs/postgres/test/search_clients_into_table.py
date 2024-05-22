from sqlalchemy.exc import IntegrityError

from os.path import abspath, dirname
import sys

sys.path.insert(0, dirname(abspath(__file__)))

from bd import SessionLocal
from entities import Client

def display_clients() -> None:
    # Criando a sessão
    session = SessionLocal()
    
    try:
        clients = session.query(Client).all()
        print("Registros na tabela Client:")
        for client in clients:
            print(f"ID: {client.id}, Email: {client.email}, Ativo: {client.is_active}")
    finally:
        session.close()
        
if __name__ == "__main__":
    display_clients()