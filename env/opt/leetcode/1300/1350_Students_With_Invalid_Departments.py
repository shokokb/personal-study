# Write your MySQL query statement below
select s.id, s.name
#, s.department_id, d.id
from Students as s
left join Departments as d
on s.department_id = d.id
where d.id is null