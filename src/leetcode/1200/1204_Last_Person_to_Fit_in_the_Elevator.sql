# Write your MySQL query statement below
WITH cte AS(
SELECT 
    person_id, 
    person_name,
    SUM(weight) OVER (ORDER BY turn) AS total,
    turn
FROM Queue)

SELECT person_name FROM cte
WHERE total <= 1000
ORDER BY turn DESC
LIMIT 1

