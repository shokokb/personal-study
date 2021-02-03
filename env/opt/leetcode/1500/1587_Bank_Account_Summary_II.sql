# Write your MySQL query statement below

SELECT u.name, SUM(amount) AS balance
FROM Transactions as t
LEFT JOIN Users as u
ON u.account = t.account
GROUP BY t.account
HAVING balance > 10000
