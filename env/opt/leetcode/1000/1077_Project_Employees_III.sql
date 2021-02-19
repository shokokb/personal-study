WITH CTE AS (
    SELECT project_id AS PID, MAX(experience_years) AS MAX_YEAR 
    FROM Project AS p
    LEFT JOIN Employee AS e
    ON p.employee_id = e.employee_id
    GROUP BY p.project_id
)

SELECT p.project_id, e.employee_id 
FROM Project AS p 
LEFT JOIN Employee As e
ON p.employee_id = e.employee_id
WHERE experience_years = 
(SELECT MAX_YEAR FROM CTE WHERE PID = p.project_id)