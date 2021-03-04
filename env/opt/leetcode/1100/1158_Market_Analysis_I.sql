# Write your MySQL query statement below
WITH cte AS(
    SELECT buyer_id, count(item_id) AS cnt
    FROM Orders
    WHERE YEAR(order_date) = 2019
    GROUP BY buyer_id
)

SELECT u.user_id AS buyer_id, u.join_date, IFNULL(c.cnt,0) AS orders_in_2019
FROM Users AS u
LEFT JOIN cte AS c
ON u.user_id = c.buyer_id
