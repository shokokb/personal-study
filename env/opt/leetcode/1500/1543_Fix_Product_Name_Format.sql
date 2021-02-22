# Write your MySQL query statement below
WITH cte AS 
(
    SELECT 
        TRIM(LOWER(product_name)) AS name, 
        DATE_FORMAT(sale_date, '%Y-%m') AS date,
        COUNT(sale_id) AS total
    FROM Sales
    GROUP BY name, date
    ORDER BY name ASC, date ASC
)

SELECT 
    name AS PRODUCT_NAME,
    date AS SALE_DATE,
    total AS TOTAL
FROM cte