import dotenv
import os

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

DB_SETTINGS = dict(
    mysql_params = dict(
        engine_name = os.getenv('MYSQL_ENGINE_NAME',''),
        user = os.getenv('MYSQL_USER',''),
        password = os.getenv('MYSQL_PASSWORD',''),
        host = os.getenv('MYSQL_HOST',''),
        port = os.getenv('MYSQL_PORT',''),
        database = os.getenv('MYSQL_DATABASE','')
        ),

postgres_params = dict(
        engine_name = os.getenv('PG_ENGINE_NAME',''),
        user = os.getenv('PG_USER',''),
        password = os.getenv('PG_PASSWORD',''),
        host = os.getenv('PG_HOST',''),
        port = os.getenv('PG_PORT',''),
        database = os.getenv('PG_DATABASE','')    
        )
    )