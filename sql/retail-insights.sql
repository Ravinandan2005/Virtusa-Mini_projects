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