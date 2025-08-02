use delhi_aqi_project;
show tables;

select * from aqi_data;

#1)) How many total records are there in the table?
select count(*) from aqi_data;

#2)) How many unique years of data do we have?
select distinct(year) from aqi_data;

#3)) Which AQI category (bucket) appears most frequently?
select aqi_bucket, count(*) as count
FROM aqi_data
group by aqi_bucket
order by count desc
limit 1;
