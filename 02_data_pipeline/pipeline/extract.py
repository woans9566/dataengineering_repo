import pandas as pd

def extractor(connection_obj,query):
    print('extractor 시작')
    df = pd.read_sql(
        sql = query,
        con = connection_obj
        )
    return df