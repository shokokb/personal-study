# Write your MySQL query statement below

WITH RECURSIVE cte as(
    SELECT task_id, 1 AS subtask_id, subtasks_count FROM Tasks
	UNION ALL
    SELECT task_id, subtask_id + 1 AS subtask_id, subtasks_count 
    FROM cte
    WHERE subtask_id < subtasks_count
)
    
SELECT c.task_id, c.subtask_id 
FROM cte c
LEFT JOIN Executed e
ON c.task_id = e.task_id AND c.subtask_id = e.subtask_id
WHERE e.subtask_id IS NULL
ORDER BY c.task_id, c.subtask_id