# Write your MySQL query statement below
WITH cte AS (
    SELECT 
        session_id,
        duration / 60 As duration
    FROM Sessions)
    
SELECT '[0-5>' AS 'bin', count(session_id) AS total FROM cte
WHERE 0 <= duration AND duration < 5
UNION ALL
SELECT '[5-10>', count(session_id) FROM cte
WHERE 5 <= duration AND duration < 10 
UNION ALL
SELECT '[10-15>', count(session_id) FROM cte
WHERE 10 <= duration AND duration < 15 
UNION ALL
SELECT '15 or more', count(session_id) FROM cte
WHERE 15 <= duration