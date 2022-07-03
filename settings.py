import os

class db_settings:
    DB_NAME = os.environ.get('DB_NAME','patent_doc')
    DB_PASSWORD = os.environ.get('DB_PASSWORD','Karim123')
    DB_USER = os.environ.get('DB_USER','postgres')
    DB_HOST = os.environ.get('DB_HOST','localhost')
    DB_PORT = os.environ.get('DB_PORT','5432')
