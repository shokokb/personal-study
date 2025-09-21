# Write your MySQL query statement below
SELECT 
    gender, 
    day, 
    SUM(score_points) OVER (partition by gender ORDER BY gender, day) AS total
FROM Scores
