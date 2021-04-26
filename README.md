# SQLAlchemy-challenge

by: Dave Wisinski

April 2021

## Project: SQL Alchemy Homework

## Description:
This project was created to demonstrate a number of data engineering and data analysis concepts using a data set of weather data (recorded precipitation and temperature values) from various weather stations in Hawaii. Data from the database was imported into a Jupyter Notebook using the SQLAlchemy ORM. Data was subsequently analyzed using Pandas DataFrames and graphs were created using the Matplotlib library.

## Additional Observations and Analysis:
- The average temperature in June (aggregated across all stations) is several degrees higher than the average temperature in December, as expected. The results of the independent (unpaired) t-test indicate that this difference is statistically significant (low p-value indicates the difference in average temperature did not occur by chance).
- The average temperature for the one year period chosen betwen June 1, 2016 and May 31, 2017 is approximately 74.39 °F. The graphically represented error bar on the output graph (indicating potential variability or "uncertainty") has a size representative of 29 degrees, as calculated by taking the period's high temperature and substracting the period's low temperature (87 °F and 58 °F, respectively).
- The average daily rainfall per weather station for the selected date range is very low, with the maximum value recorded at the station which also has the highest elevation.
- Based on the data available, the average temperature for the first week of June (aggregated across all stations) is approximately 74.57 °F.

## **Important Notes:**
Source data (SQLite database and .csv files) located in the Resources folder. 