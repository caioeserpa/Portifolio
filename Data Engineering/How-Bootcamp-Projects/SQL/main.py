from sqlalchemy import create_engine
import pandas as pd

engine =create_engine(
    'postgresql+psycopg2://root:root@localhost/raw'
)

sql ="""
SELECT * from vw_artist;

"""


df_query = pd.read_sql_query(sql,engine)

df_query_song =  pd.read_sql_query("select * from vw_song",
                                    engine)


insert_query = """
insert into tb_artist(
select t1."date",
t1."rank",
t1.artist,
t1.song
from public."Billboard" as t1
where t1.artist like 'Nirvana%'
order by t1.artist, t1.song, t1."date");

"""
engine.execute(insert_query)