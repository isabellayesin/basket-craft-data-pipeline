# %%
# import necessary libraries
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# %%
#load environment variables from .env file
load_dotenv()

os.environ['MYSQL_USER']

 # %%
mysql_user = os.environ['MYSQL_USER']
mysql_password = os.environ['MYSQL_PASSWORD']
mysql_host = os.environ['MYSQL_HOST']
mysql_db = os.environ['MYSQL_DB']

# %%
pg_user = os.environ['MYSQL_USER']
pg_password = os.environ['MYSQL_PASSWORD']
pg_host = os.environ['MYSQL_HOST']
pg_db = os.environ['MYSQL_DB']

pg_db


# %%
mysql_user = 'analyst'
mysql_password = 'go_lions'
mysql_host = 'db.isba.co'
mysql_db = 'basket_craft'

# %%
pg_user = 'postgres'
pg_password = 'isba_4715'
pg_host = 'isba-dev-02.cipysukaajmj.us-east-1.rds.amazonaws.com'
pg_db = 'basket_craft'

# %%
mysql_conn_str = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'
pg_conn_str = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'

# %%
#create datbase engines
mysql_engine = create_engine(mysql_conn_str)
pg_engine = create_engine(pg_conn_str)

# %%
# read orders from mysql
# Read website_sessions from MySQL for December 2023
df = pd.read_sql(
    "SELECT * FROM website_sessions WHERE created_at BETWEEN '2023-12-01' AND '2023-12-31 23:59:59';",
    mysql_engine
)

# %%
# df

# %%
#write dataframe to products table in postgres (raw schema)
df.to_sql('website_sessions', pg_engine, schema='raw', if_exists='append', index=False)


# %%
print(f'{len(df)} records loaded into postgres into raw.website_sessions table.')


