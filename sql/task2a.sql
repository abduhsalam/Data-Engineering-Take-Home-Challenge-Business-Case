// Cleaning sales_raw

CREATE TABLE customers_clean AS
SELECT
  id,
  name,
  CASE
    WHEN dob = '1900-01-01' THEN NULL
    WHEN dob LIKE '%/%/%' THEN STR_TO_DATE(dob, '%d/%m/%Y')
    WHEN dob LIKE '%-%-%' THEN STR_TO_DATE(dob, '%Y-%m-%d')
    ELSE NULL
  END AS dob,
  created_at
FROM customers_raw;


// Cleaning after_sales_raw

CREATE TABLE sales_clean AS
SELECT
  vin,
  customer_id,
  model,
  invoice_date,
  CAST(REPLACE(price, '.', '') AS UNSIGNED) AS price,
  created_at
FROM sales_raw;


// Cleaning customer_addresses_raw

CREATE TABLE after_sales_clean AS
SELECT a.*
FROM after_sales_raw a
INNER JOIN customers_clean c 
  ON a.customer_id = c.id
WHERE 
  a.vin IS NOT NULL
  AND a.service_date IS NOT NULL;


// Cleaning customer_addresses_raw

CREATE TABLE customer_addresses_clean AS
SELECT
  customer_id,
  address,
  INITCAP(city) AS city,
  INITCAP(province) AS province,
  created_at
FROM customer_addresses_raw;
