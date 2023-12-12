-- 1
SELECT p.product_name, s.year, s.price FROM Sales s JOIN Product p ON s.product_id = p.product_id;

-- 2
SELECT p.product_name, s.year, s.price FROM Sales s, Product p WHERE s.product_id = p.product_id;