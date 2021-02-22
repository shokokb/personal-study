# Write your MySQL query statement below
SELECT 
    gender, 
    day, 
    (SELECT sum(score_points) FROM Scores AS s2 
        WHERE s2.gender = s1.gender 
        AND   s2.day <= s1.day) 
    as total
FROM Scores AS s1
GROUP BY gender, day
ORDER BY gender, day
