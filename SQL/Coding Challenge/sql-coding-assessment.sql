create database sql_coding_challenge_1;
use sql_coding_challenge_1;

-- Creating the tables
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- Inserting sample data
INSERT INTO employees (employee_id, first_name, last_name, department_id)
VALUES
    (1, 'John', 'Doe', 1),
    (2, 'Jane', 'Smith', 2),
    (3, 'Bob', 'Johnson', 1),
    (4, 'Alice', 'Brown', 2),
    (5, 'Chris', 'Lee', 3);

INSERT INTO departments (department_id, department_name)
VALUES
    (1, 'HR'),
    (2, 'IT'),
    (3, 'Marketing');



-- Inner Join
SELECT
    employees.employee_id,
    employees.first_name,
    employees.last_name,
    employees.department_id,
    departments.department_name
FROM
    employees
INNER JOIN
    departments ON employees.department_id = departments.department_id;
    
    -- Left Join
    SELECT
    employees.employee_id,
    employees.first_name,
    employees.last_name,
    employees.department_id,
    departments.department_name
FROM
    employees
LEFT JOIN
    departments ON employees.department_id = departments.department_id;

-- Right Join
SELECT
    employees.employee_id,
    employees.first_name,
    employees.last_name,
    employees.department_id,
    departments.department_name
FROM
    employees
RIGHT JOIN
    departments ON employees.department_id = departments.department_id;

-- Self Join

SELECT
    e1.employee_id AS emp_id1,
    e1.first_name AS first_name1,
    e1.last_name AS last_name1,
    e1.department_id AS dept_id1,
    e2.employee_id AS emp_id2,
    e2.first_name AS first_name2,
    e2.last_name AS last_name2,
    e2.department_id AS dept_id2
FROM
    employees e1
JOIN
    employees e2 ON e1.department_id = e2.department_id
WHERE
    e1.employee_id <> e2.employee_id;

-- Cross Join
SELECT
    employees.employee_id,
    employees.first_name,
    employees.last_name,
    departments.department_id,
    departments.department_name
FROM
    employees
CROSS JOIN
    departments;

-- Equi Join
SELECT
    employees.employee_id,
    employees.first_name,
    employees.last_name,
    employees.department_id,
    departments.department_name
FROM
    employees
JOIN
    departments ON employees.department_id = departments.department_id;

-- Non Equi Join
SELECT
    employees.employee_id,
    employees.first_name,
    employees.last_name,
    employees.department_id,
    departments.department_name
FROM
    employees
JOIN
    departments ON employees.department_id <> departments.department_id;

-- Natural Join
SELECT
    employee_id,
    first_name,
    last_name,
    department_id,
    department_name
FROM
    employees
NATURAL JOIN
    departments;

-- creating  sales table
CREATE TABLE sales (
    product VARCHAR(50),
    category VARCHAR(50),
    amount DECIMAL(10, 2)
);

INSERT INTO sales (product, category, amount) VALUES
    ('Product1', 'Category1', 100.00),
    ('Product2', 'Category1', 150.00),
    ('Product3', 'Category2', 120.00),
    ('Product4', 'Category2', 200.00),
    ('Product5', 'Category1', 180.00);

-- subtotal query
SELECT
    category,
    product,
    SUM(amount) AS subtotal_amount
FROM
    sales
GROUP BY
    category, product
WITH ROLLUP;

-- Using OVER and PARTITION BY for Total Aggregation:
SELECT
    product,
    category,
    amount,
    SUM(amount) OVER (PARTITION BY category) AS total_category_amount
FROM
    sales;


