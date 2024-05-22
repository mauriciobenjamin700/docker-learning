from sqlalchemy import text

from os.path import abspath, dirname
import sys

sys.path.insert(0, dirname(abspath(__file__)))

from bd import SessionLocal

# Função para verificar se um banco de dados específico existe
def check_database_exists(db_name):
    # Criando uma nova sessão
    session = SessionLocal()
    try:
        # Consulta para listar bancos de dados
        result = session.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false;"))
        databases = [row[0] for row in result]  # Acessa o primeiro elemento da tupla

        # Verificando se o banco de dados desejado está na lista
        if db_name in databases:
            print(f"O banco de dados '{db_name}' existe.")
        else:
            print(f"O banco de dados '{db_name}' não existe.")
    finally:
        # Fechando a sessão
        session.close()

if __name__ == "__main__":
    # Verificando se um banco de dados específico existe
    check_database_exists("postgres")
