# Write your MySQL query statement below

SELECT DISTINCT buyer_id 
FROM Sales
WHERE buyer_id IN     
    (SELECT buyer_id From Sales WHERE product_id = (
        SELECT product_id From Product WHERE product_name = 'S8'))
AND   buyer_id NOT IN 
    (SELECT buyer_id From Sales WHERE product_id = (
        SELECT product_id From Product WHERE product_name = 'iPhone'))
ORDER BY buyer_id
