# Write your MySQL query statement below
with
  TeamSize as 
    (
        select team_id, count(employee_id) as team_size 
        from Employee
        group by team_id
    )

select e.employee_id, t.team_size 
from Employee as e left join TeamSize as t
on e.team_id = t.team_id;
