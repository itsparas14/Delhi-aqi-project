#STEP 1: Purpose: Work only with Delhi's air quality
# filtering delhi by city column

import pandas as pd

df= pd.read_csv("Delhi_aqi_project/city_day.csv/01.city_day.csv")

#filtering out for city= DELHI
delhi_df= df[df["City"]=="Delhi"].copy()
print(delhi_df)

delhi_df.to_csv("delhi_filtered.csv",index = False)














