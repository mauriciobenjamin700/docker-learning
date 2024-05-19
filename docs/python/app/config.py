import os

class Config:
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'postgres')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'my-postgres')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)
