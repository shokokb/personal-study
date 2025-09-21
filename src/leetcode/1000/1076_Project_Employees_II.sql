SELECT project_id
  FROM(
        SELECT project_id,
               RANK()OVER(ORDER BY COUNT(employee_id)DESC) AS rnk
          FROM Project
         GROUP BY 1) AS A
 WHERE rnk = 1 

