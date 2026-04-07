-- create database
CREATE DATABASE retail_insights;

-- create categories table
CREATE TABLE categories (category_id SERIAL PRIMARY KEY, category_name VARCHAR(100));

-- create products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(150),
    category_id INT REFERENCES categories(category_id),
    price DECIMAL(10,2),
    stock_count INT,
    expiry_date DATE
);

-- create sales transactions table
CREATE TABLE sales_transactions (
    transaction_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(product_id),
    quantity_sold INT,
    transaction_date DATE
);

-- insert categories
INSERT INTO categories (category_name) VALUES
('Dairy'),
('Beverages'),
('Snacks'),
('Household');

-- insert products
INSERT INTO products (product_name, category_id, price, stock_count, expiry_date) VALUES
('Milk', 1, 50.00, 120, CURRENT_DATE + INTERVAL '5 days'),
('Cheese', 1, 200.00, 30, CURRENT_DATE + INTERVAL '20 days'),
('Coke', 2, 45.00, 200, CURRENT_DATE + INTERVAL '60 days'),
('Chips', 3, 20.00, 10, CURRENT_DATE + INTERVAL '15 days'),
('Detergent', 4, 150.00, 80, CURRENT_DATE + INTERVAL '365 days');

-- insert sales data
INSERT INTO sales_transactions (product_id, quantity_sold, transaction_date) VALUES
(1, 10, CURRENT_DATE - INTERVAL '2 days'),
(1, 5, CURRENT_DATE - INTERVAL '10 days'),
(2, 2, CURRENT_DATE - INTERVAL '40 days'),
(3, 20, CURRENT_DATE - INTERVAL '5 days'),
(4, 1, CURRENT_DATE - INTERVAL '70 days');