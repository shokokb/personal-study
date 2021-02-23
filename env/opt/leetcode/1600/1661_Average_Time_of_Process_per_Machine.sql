# Write your MySQL query statement below
with cte as (
SELECT  
    machine_id,     
    process_id,
    SUM(CASE WHEN activity_type = 'start' THEN -timestamp
    ELSE +timestamp END) AS time
FROM Activity    
GROUP BY machine_id, process_id
)

SELECT machine_id, ROUND(AVG(time), 3) as processing_time 
FROM cte
GROUP BY machine_id
