from os.path import abspath, dirname
import sys

sys.path.insert(0, dirname(abspath(__file__)))

from bd import SessionLocal
from entities import Client

def check_client_existence(client_id:int) -> None:

    session = SessionLocal()
    
    try:
        client = session.query(Client).filter(Client.id == client_id).first()
        print(client.email)
        if client:
            print(f"O registro com o ID {client_id} existe.")
        else:
            print(f"O registro com o ID {client_id} não existe.")
    finally:
        session.close()
        
if __name__ == "__main__":
    check_client_existence(3)