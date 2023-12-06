-- SQL Queries 


-- Task 1:

SELECT country_code, count (country_code)
FROM dim_store_details
WHERE address IS NOT null
GROUP BY country_code
ORDER BY count DESC;


-- Task 2:

SELECT locality, count (locality) 
FROM dim_store_details
GROUP BY locality
ORDER BY count DESC
LIMIT 7;


-- Task 3:

SELECT ROUND(SUM(orders_table.product_quantity * dim_products.product_price)::numeric, 2) AS total_sales,
EXTRACT (MONTH FROM dim_date_times.datetimes) AS month
FROM dim_products
INNER JOIN orders_table ON dim_products.product_code = orders_table.product_code
INNER JOIN dim_date_times
ON orders_table.date_uuid = dim_date_times.date_uuid
GROUP BY month
ORDER by total_sales DESC
LIMIT 6;


-- Task 4:

SELECT
COUNT ("index") AS number_of_sales,
SUM (product_quantity) AS product_quantity_count,
CASE
WHEN store_code = 'WEB-1388012W' THEN 'Web' 
ELSE 'Offline'
END AS "location"
FROM orders_table
GROUP BY location
ORDER BY location DESC;


-- Task 5:

SELECT dim_store_details.store_type AS store_type,
ROUND (SUM(product_quantity * dim_products.product_price)::numeric, 2) AS total_sales,
ROUND ((SUM(product_quantity * dim_products.product_price) / 
(SELECT SUM(product_quantity * dim_products.product_price)
FROM orders_table
LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code) * 100)::numeric, 2) AS "percentage_total(%)"
FROM orders_table
LEFT JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY store_type
ORDER BY total_sales DESC;


-- Task 6:

SELECT ROUND(SUM(product_quantity * dim_products.product_price)::numeric, 2) AS total_sales,
EXTRACT (YEAR FROM dim_date_times.datetimes) AS year,
EXTRACT (MONTH FROM dim_date_times.datetimes) AS month
FROM orders_table
LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code
LEFT JOIN dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
GROUP BY month,year
ORDER BY total_sales DESC
LIMIT 10;


-- Task 7:

SELECT SUM(staff_numbers) AS total_staff_numbers,country_code
FROM dim_store_details
GROUP BY country_code
ORDER BY total_staff_numbers DESC;


-- Task 8:

SELECT ROUND(SUM(product_quantity * dim_products.product_price)::numeric, 2) AS total_sales,
dim_store_details.store_type AS store_type,
dim_store_details.country_code AS country_code
FROM orders_table
JOIN dim_products ON orders_table.product_code = dim_products.product_code
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE dim_store_details.country_code = 'DE'
GROUP BY store_type,country_code
ORDER BY total_sales;


-- Task 9:

SELECT year,
FORMAT('"hours": %s, "minutes": %s, "seconds": %s, "milliseconds": %s', 
EXTRACT (HOUR FROM actual_time_taken), EXTRACT (MINUTE FROM actual_time_taken),
EXTRACT (SECOND FROM actual_time_taken), EXTRACT (MILLISECOND FROM actual_time_taken)) actual_time_taken
FROM(
SELECT
EXTRACT (YEAR FROM dim_date_times.datetimes) AS year,
(MAX(datetimes) - MIN(datetimes)) / (COUNT(*) - 1) AS actual_time_taken
FROM dim_date_times
GROUP BY year
ORDER BY actual_time_taken DESC
) x
