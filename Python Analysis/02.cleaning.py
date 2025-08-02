#STEP 2: Convert Date Column and creating time columns


import pandas as pd

filtered_delhi= pd.read_csv("Delhi_aqi_project/city_day.csv/02.delhi_filtered.csv")

filtered_delhi['Date']= pd.to_datetime(filtered_delhi['Date'])

filtered_delhi['Year'] = filtered_delhi['Date'].dt.year
filtered_delhi['Month']= filtered_delhi['Date'].dt.month

#changing the month names takes different methodology such as: strfttime(), stand for: string format time!
filtered_delhi['Month_name'] = filtered_delhi['Date'].dt.strftime('%B')

print(filtered_delhi)

filtered_delhi.to_csv("converted_dt_delhi.csv",index= False)

#for checking if the conversion was succesful or not
# print(delhi_df['Date'].dtypes)

#extracts the year from the date
# df_2= pd.to_datetime('2025-10-21').month







