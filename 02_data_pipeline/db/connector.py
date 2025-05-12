import pymysql, psycopg2
from sqlalchemy import create_engine

class DOConnector:
    def __init__(self, engine_name, user, password, host, port, database):
        self.engine_name = engine_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
    
    def pymysql_connection(self):
        mysql_conn = pymysql.connect(
            user =self.user,
            password=self.password,
            host=self.host,
            port=int(self.port),
            database=self.database,
            charset='utf8'
            )
        return mysql_conn

    def psycopg2_connection(self):
        psycopg2_conn = psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
            )
        return psycopg2_conn
    
    def sqlalchemy_connection(self):
        sqlalchemy_conn = create_engine(f"{self.engine_name}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        return sqlalchemy_conn