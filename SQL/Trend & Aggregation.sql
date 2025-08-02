-- 📊 Trend & Aggregation:

select * from aqi_data;
# 4) Find the average AQI for each year.
select year, avg(AQI) as avg_aqi from aqi_data
group by year
order by avg_aqi desc ;

#5)) which year had the highest avg aqi?
select year, avg(AQI) as avg_aqi from aqi_data
group by year
order by avg_aqi desc ;

# with subquery:-

#6)What is the average AQI for each month,
#across all years?

select month_name, round(avg(aqi),2) as month_wise_aqi 
FROM aqi_data
group by month_name
order by month_wise_aqi desc;

#7)) Show monthly AQI trend for each year.
select year, month_name, round(avg(aqi),2) 
FROM aqi_data
group by month_name, year
order by month_name, year;


