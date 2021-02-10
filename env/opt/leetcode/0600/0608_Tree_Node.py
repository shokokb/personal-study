# Write your MySQL query statement below
SELECT 
    DISTINCT t1.id AS id,
    CASE WHEN t1.p_id IS NULL THEN 'Root'
         WHEN t2.id IS NULL THEN 'Leaf'
         ELSE 'Inner' 
    END AS Type
FROM tree AS t1
LEFT JOIN tree AS t2
ON t1.id = t2.p_id