#handling the missing values using fillna() and dropa()

import pandas as pd

cleaned_delhi_aqi = pd.read_csv("Delhi_aqi_project/city_day.csv/03.delhi_aqi_datetime_converted.csv")


# print(cleaned_delhi_aqi)


#to find the sum of null values in each column #########
# print(cleaned_delhi_aqi.isnull().sum())


#to see if a specific column is null
# null_values_delhi_aqi = cleaned_delhi_aqi[cleaned_delhi_aqi['AQI'].isnull()]

# print(null_values_delhi_aqi)

#dropping the null values
delhi_aqi_no_nulls= cleaned_delhi_aqi.dropna()
print(delhi_aqi_no_nulls)

#to find total null values in the entire dataframe:
# print(delhi_df.isnull().sum().sum())

delhi_aqi_no_nulls.to_csv('delhi_aqi_cleaned.csv')