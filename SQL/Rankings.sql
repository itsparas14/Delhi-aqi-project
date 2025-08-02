#8))Which were the top 5 most polluted days in Delhi 
#(based on AQI)?

select * from aqi_data;
#DAYS|YEAR|MONTH|AQI|RANKING!

select
	AQI, 
	day(date) as day,
	year(date) as year,
	monthname(date) as month
FROM
	(select
	date,
	aqi,
	rank() over(partition by year(date),monthname(date)
	order by aqi desc)
	as ranked_aqi
FROM 
	aqi_data 
	) as ranked_table
	where ranked_aqi <=5
	limit 5;


#9) Which were the top 5 cleanest days in Delhi?

#DAYS|AQI|RANKIING

SELECT
day(date),
AQI
FROM(
SELECT
	date,
    AQI,
    RANK() OVER(PARTITION BY day(date)
    ORDER BY aqi ASC) as ranked_aqi
    FROM aqi_data
) as ranked_table
where ranked_aqi <=5
limit 5;








