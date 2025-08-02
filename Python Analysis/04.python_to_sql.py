from sqlalchemy import create_engine
import pandas as pd

#reading csv file
df= pd.read_csv("Delhi_aqi_project/city_day.csv/04.delhi_aqi_cleaned.csv")

password ="1234"

#creating SQL ALCHMEY ENGINE
engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost/delhi_aqi_project')

#🧠 Tip: Use if_exists='append' if you're importing more data later without replacing the table.
df.to_sql(name='aqi_data',con= engine,if_exists='replace',index=False)

print("Data uploaded successfully")

# Quick MySQL connection test
# with engine.connect() as connection:
#     print("Connected:", connection)
