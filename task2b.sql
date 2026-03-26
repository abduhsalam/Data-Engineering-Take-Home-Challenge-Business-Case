// Reporting Query #1 (Sales by Class & Model)

SELECT
  DATE_FORMAT(invoice_date, '%Y-%m') AS periode,
  CASE
    WHEN price BETWEEN 100000000 AND 250000000 THEN 'LOW'
    WHEN price BETWEEN 250000001 AND 400000000 THEN 'MEDIUM'
    WHEN price > 400000000 THEN 'HIGH'
  END AS class,
  model,
  SUM(price) AS total
FROM sales_clean
GROUP BY 1,2,3;


// Reporting Query #2 (Service Count + Priority)

SELECT
  YEAR(a.service_date) AS periode,
  a.vin,
  c.name AS customer_name,
  addr.address,
  COUNT(*) AS count_service,
  CASE
    WHEN COUNT(*) > 10 THEN 'HIGH'
    WHEN COUNT(*) BETWEEN 5 AND 10 THEN 'MED'
    ELSE 'LOW'
  END AS priority
FROM after_sales_clean a
LEFT JOIN customers_clean c ON a.customer_id = c.id
LEFT JOIN customer_addresses_clean addr ON a.customer_id = addr.customer_id
GROUP BY 1,2,3,4;