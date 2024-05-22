from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:3000/postgres"

# Criando o motor de conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criando uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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

# Verificando se um banco de dados específico existe
check_database_exists("nome_do_banco_desejado")
