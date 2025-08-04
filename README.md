# Delhi Air Quality Index (AQI) Data Analysis

This repository contains a comprehensive data analysis project focused on examining the air quality of Delhi using AQI data. The aim of this project is to identify patterns, uncover insights, and visualize the severity and trends of air pollution in Delhi using industry-standard tools and methods.

## Project Objective

To analyze real-time air quality data of Delhi in order to:
- Understand pollution trends across various seasons and regions
- Quantify the levels of key pollutants such as PM2.5, PM10, NO2, SO2, CO, and O3
- Create data-driven visualizations and dashboards for public awareness and professional demonstration

## Dataset Overview

- Total Rows: 1,500+
- Columns: Date, Location, AQI, PM2.5, PM10, NO2, SO2, CO, O3, and others
- Time Range: January 2014 to June 2020]
- Format: CSV

## Tools and Technologies Used

- Python (Pandas, Matplotlib, Seaborn)
- SQL (for data filtering, aggregation, and querying)
- Microsoft Excel (initial inspection and data manipulation)
- Power BI (for interactive dashboard creation)

## Project Workflow

### Data Collection
Collected air quality data from a reliable source. Imported the data into Python and Excel for initial inspection.

### Data Cleaning and Preprocessing
- Used Pandas to handle missing values, clean column names, and convert data types
- Removed or imputed null values to ensure data consistency
- Standardized date formats and pollutant measurement units

### Exploratory Data Analysis
- Conducted statistical analysis to observe average, minimum, and maximum pollutant levels
- Identified seasonal spikes and region-specific trends
- Plotted time-series trends and pollutant distribution using Matplotlib and Seaborn

### SQL Integration
- Executed queries to segment data based on time period and location
- Used filtering, grouping, and joins to extract actionable insights from structured data

### Dashboard Creation
- Developed a dynamic dashboard in Power BI
- Included multi-dimensional filtering options based on time, pollutant, and area
- Visualized trends for easier interpretation by both technical and non-technical audiences

## Key Insights

- PM2.5 and PM10 levels were consistently above safe limits, especially during winter months
- Air quality declined significantly around major festivals such as Diwali
- Certain zones such as Anand Vihar and Rohini exhibited higher average AQI than others
- Strong correlation observed between PM2.5 and overall AQI

## Deliverables

- Cleaned and processed dataset (CSV)
- Python scripts for analysis and visualization
- SQL scripts for querying structured data
- Power BI dashboard for interactive exploration
- Final report and visual summary posted on LinkedIn and GitHub

## How to Use This Repository

1. Clone the repository
2. Open the Jupyter Notebook or Python scripts in your local IDE
3. Run the code using the provided dataset
4. Explore the insights or customize the visualizations
5. Use the Power BI dashboard file to interact with live visuals

## Repository Structure

- data/ — Raw and cleaned datasets
- notebooks/ — Python notebooks and scripts
- sql/ — SQL scripts used for data queries
- visuals/ — Screenshots and Power BI dashboard files
- README.md — Project documentation

## Author

Paras Kumar  
LinkedIn: https://www.linkedin.com/in/paraskumar14/  
GitHub: https://github.com/itsparas14

