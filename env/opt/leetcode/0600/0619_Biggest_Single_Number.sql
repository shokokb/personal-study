# Write your MySQL query statement below
WITH cte AS (
    SELECT num
    FROM my_numbers
    GROUP BY num
    HAVING count(num) = 1
    ORDER BY num DESC
    LIMIT 1
)

SELECT 
    CASE WHEN count(num) = 0 THEN NULL
    ELSE num END AS num
FROM cte
