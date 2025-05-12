from settings import DB_SETTINGS
from db.connector import DOConnector
from pipeline.extract import extractor
from pipeline.transform import transformer
from pipeline.load import loader

def main():
    print('데이터 파이프라인 시작')
    mysql_conn = DOConnector(**DB_SETTINGS['mysql_params']).sqlalchemy_connection()
    query = 'SELECT * FROM pokemon'
    pg_conn = DOConnector(**DB_SETTINGS['postgres_params']).sqlalchemy_connection()
    table_name='pokemon_type'

    # 함수 실행부부
    df = extractor(mysql_conn,query)
    t_df = transformer(df)
    loader(t_df,table_name,pg_conn)
    print('데이터 파이프라인 종료')
    
main()