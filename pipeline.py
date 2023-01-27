import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")
engine.connect()

df1 = pd.read_csv("green_tripdata_2019-01.csv", nrows=100)
df2 = pd.read_csv("taxi+_zone_lookup.csv", nrows=100)

df1.head(n=0).to_sql(name="green_taxi_data", con=engine, if_exists="replace")
df2.to_sql(name="zone_lookup", con=engine, if_exists="replace")

df1_iter = pd.read_csv("green_tripdata_2019-01.csv", iterator=True, chunksize=100000)
while True:
  df1 = next(df1_iter)
  df1.to_sql(name="green_taxi_data", con=engine, if_exists="append")