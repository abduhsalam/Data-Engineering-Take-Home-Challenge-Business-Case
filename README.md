# 🚀 Maju Jaya Data Engineering Take-Home Challenge

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

This project implements a simple **data engineering pipeline** for a retail automotive company **Maju Jaya**, covering ingestion, transformation, and reporting.

---

# 🎯 Objective

- Ingest daily CSV files into MySQL
- Clean and standardize raw data
- Build datamart-ready queries
- Containerize the full pipeline

---

# 🏗️ Architecture

```
        +---------------------+
        |  CSV (Daily Files)  |
        +----------+----------+
                   |
                   v
        +---------------------+
        |   Python ETL        |
        +----------+----------+
                   |
                   v
        +---------------------+
        |   MySQL (Raw)       |
        +----------+----------+
                   |
                   v
        +---------------------+
        |   Clean Layer       |
        +----------+----------+
                   |
                   v
        +---------------------+
        |   Datamart          |
        +---------------------+
```

---

# 📁 Project Structure

```
project/
├── docker-compose.yml          # Orchestration config
├── README.md                   # Documentation
├── sql/                        # SQL scripts
│   ├── 01_init_schema.sql
│   ├── 02_cleaning.sql
│   └── 03_datamart_queries.sql
├── data/                       # Input data
│   └── customer_addresses/
│       └── customer_addresses_20260301.csv
└── etl/                        # ETL logic
    ├── Dockerfile
    ├── requirements.txt
    └── ingest_customer_addresses.py
```

---

# ⚙️ Tech Stack

- Python (Pandas, SQLAlchemy)
- MySQL 8
- Docker Compose

---

# 🚀 How to Run

## 1. Prepare data folder

```
mkdir -p data/customer_addresses
```

Place CSV file:
```
data/customer_addresses/customer_addresses_20260301.csv
```

---

## 2. Run pipeline

```
docker compose up --build
```

---

## 3. Expected output

```
MySQL is ready.
Loading: /app/data/customer_addresses/customer_addresses_20260301.csv
Load completed.
```

---

# 🧠 ETL Behavior

- Batch process (runs once)
- Reads latest CSV file
- Inserts into `customer_addresses_raw`
- Stops after completion (no restart)

---

# 🗄️ Database Access

```
docker exec -it majujaya-mysql mysql -u dw_user -p
```

Password:
```
dw_password
```

---

# 🖥️ HeidiSQL Connection

## Local setup

- Host: 127.0.0.1  
- Port: 3306  
- User: dw_user  
- Password: dw_password  

---

# 🔄 Reset Database

```
docker compose down -v
docker compose up --build
```

---

# 🧹 Data Cleaning Highlights

- Invalid DOB (`1900-01-01`) → NULL
- Multiple date formats normalized
- Price string → numeric conversion
- Province standardization (DKI Jakarta)
- Data validation for customer_id and VIN

---

# 📊 Datamart Output

## Sales Report

- periode (YYYY-MM)
- class (LOW / MEDIUM / HIGH)
- model
- total

## After Sales Report

- periode (YYYY)
- vin
- customer_name
- address
- count_service
- priority

---

# 🚀 Future Improvements

- Incremental ingestion (avoid duplicates)
- File archival after processing
- Scheduler (Airflow / cron)
- Logging & monitoring
- CI/CD integration

---

# 👤 Author

Data Engineering Take-Home Submission
