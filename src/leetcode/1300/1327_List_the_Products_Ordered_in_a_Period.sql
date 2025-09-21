# Write your MySQL query statement below

SELECT p.product_name, sum(o.unit) AS unit
From Orders AS o
LEFT JOIN Products AS p
ON p.product_id = o.product_id
WHERE order_date LIKE '2020-02%'
GROUP BY p.product_id
HAVING unit >= 100
