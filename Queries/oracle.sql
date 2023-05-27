--Query 1
SELECT p.product_id, p.product_name, s.quantity FROM product p
JOIN stock s ON p.product_id = s.product_id
ORDER BY s.quantity DESC
FETCH FIRST 1 ROWS ONLY;

--Query 2
SELECT u.user_id, SUM(od.total) AS total_spent
FROM store_users u
JOIN order_details od ON u.user_id = od.user_id
GROUP BY u.user_id
ORDER BY total_spent DESC
FETCH FIRST 1 ROWS ONLY;

--Query 3
SELECT d.department_id, d.department_name, e.salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
ORDER BY e.salary DESC
FETCH FIRST 1 ROWS ONLY;

--Query 4
SELECT COUNT(DISTINCT province) AS num_provinces
FROM addresses
JOIN order_details ON addresses.adress_id = order_details.delivery_adress_id;

--Query 5
SELECT d.department_id, d.department_name, COUNT(*) AS num_employees
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY num_employees DESC
FETCH FIRST 1 ROWS ONLY;

--Query 6
SELECT pc.category_id, pc.category_name, MAX(d.discount_percent) AS max_discount_percent
FROM product_categories pc
JOIN product p ON pc.category_id = p.category_id
JOIN discount d ON p.discount_id = d.discount_id
GROUP BY pc.category_id, pc.category_name
ORDER BY max_discount_percent DESC
FETCH FIRST 1 ROWS ONLY;

--Query 7
SELECT COUNT(*) AS total_enconendas_paypal
FROM payment_details
WHERE provider = 'PayPal';

--Query 8
SELECT s.session_id, COUNT(*) AS total_produtos
FROM shopping_session s
JOIN cart_item c ON s.session_id = c.session_id
GROUP BY s.session_id
ORDER BY total_produtos DESC
FETCH FIRST 1 ROW ONLY;


