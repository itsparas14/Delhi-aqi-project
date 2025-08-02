#10)) Pollutant Analysis
#What is the average PM2.5 and PM10 
#concentration for each year?

use delhi_aqi_project;
select * from aqi_data;

SELECT
	year, 
    ROUND(avg(NO2),2) as Avg_NO2,
    ROUND(avg(PM10),2) as Avg_PM10 
    FROM aqi_data
    GROUP BY year
    ORDER BY year;