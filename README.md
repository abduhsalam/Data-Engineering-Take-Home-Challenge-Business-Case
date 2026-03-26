# Maju Jaya Data Engineering Take-Home Challenge

This project is created to answer the Data Engineering take-home challenge for the business case of retail automotive company Maju Jaya.

## Objective
- Ingest daily CSV files into MySQL
- Clean raw data
- Build datamart queries
- Design simple data warehouse
- Run using Docker Compose

## Project Structure
.
├── docker-compose.yml
├── README.md
├── sql
│   ├── 01_init_schema.sql
│   ├── 02_cleaning.sql
│   └── 03_datamart_queries.sql
├── data
│   └── customer_addresses
│       └── customer_addresses_20260301.csv
└── etl
    ├── Dockerfile
    ├── requirements.txt
    └── ingest_customer_addresses.py

## How to Run

1. Prepare folder:
mkdir -p data/customer_addresses

2. Put CSV file:
data/customer_addresses/customer_addresses_20260301.csv

3. Run:
docker-compose up --build

## Pipeline Flow
CSV → Python ETL → MySQL Raw → Clean Layer → Datamart

## Notes
- Handles dirty DOB like 1900-01-01 → NULL
- Converts price to numeric
- Validates customer_id and VIN

## Author
Data Engineering Take-Home Submission
