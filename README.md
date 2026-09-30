# DataForge

## Enterprise Retail Data Engineering & Analytics Platform

DataForge is an end-to-end data engineering project that collects, cleans, validates, transforms, stores, and analyzes retail data.

## Project Objectives

- Build an end-to-end retail data pipeline
- Ingest data from raw sources
- Clean and transform data using Python
- Implement data quality checks
- Store data in a relational database
- Build a data warehouse using Snowflake
- Perform analytical queries using SQL
- Create interactive dashboards using Power BI
- Implement incremental data loading
- Document and test the complete pipeline

## Technology Stack

- Python
- Pandas
- NumPy
- SQL
- MySQL
- Snowflake
- Power BI
- Git & GitHub

## Project Architecture

Raw Data
   ↓
Data Ingestion
   ↓
Data Cleaning & Validation
   ↓
Transformation
   ↓
MySQL
   ↓
Snowflake Data Warehouse
   ↓
SQL Analytics
   ↓
Power BI Dashboard

## Project Status

🚧 Project setup completed.

The data engineering pipeline is currently under development.

## Data Quality Findings

### Initial Dataset Findings

The raw Amazon retail dataset contains 128,975 rows and 24 columns.

Initial validation identified:

- Unnecessary columns: `index`, `Unnamed: 22`
- Missing values in `Amount`
- Missing values in `currency`
- Missing values in shipping-related columns
- Large number of missing values in `promotion-ids`
- Large number of missing values in `fulfilled-by`
- No complete duplicate rows were found
- Date values were successfully validated