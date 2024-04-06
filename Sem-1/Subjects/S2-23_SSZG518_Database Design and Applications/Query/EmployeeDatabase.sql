show databases;

-- Create a new database (if not already created)
CREATE DATABASE IF NOT EXISTS EmployeeDatabase;
 
-- Select the database to use
USE EmployeeDatabase;
 
-- Create a new table with the specified schema
CREATE TABLE Employee (
   Emp_no INT,
   Name VARCHAR(30),
   Dept_ID VARCHAR(10),
   Basic INT,
   HRA INT,
   Deduction INT,
   TAX INT
);
show tables;

INSERT INTO Employee (Emp_no, Name, Dept_ID, Basic, HRA, Deduction, TAX) VALUES
(1, 'Rakesh', 'D1', 5000, 4000, 300, 10),
(2, 'Prasanna', 'D2', 4500, 3800, 290, 10),
(3, 'Sham', 'D3', 3000, 1200, 250, 10),
(4, 'Rajesh', 'D1', 4500, 4000, 350, 12),
(5, 'Gautam', 'D2', 5500, 1000, 200, 15),
(6, 'Ram', 'D3', 6500, 1500, 250, 20);

alter table Employee 
add primary key (Emp_no);
 
select * from Employee;
 
desc Employee;
 
select count(*) from Employee;
 
select count(name) from Employee;
 
select count(dept_id) from Employee;
 
select count(distinct dept_id) from Employee;
 
-- number of employees in department d1 with salary < 6000
 
select count(name) 
from Employee
where dept_id = 'D1' and Basic < 6000;
 
select * from Employee
where dept_id = 'D1' and Basic= 4500;
 
SET SQL_SAFE_UPDATES = 0;
 
update Employee
SET Basic = 45000
Where dept_id = 'D1' and Basic = 4500;
 
SET SQL_SAFE_UPDATES = 1;
 
 
UPDATE Employee
SET Basic = 45000
WHERE dept_id = 'D1' AND Basic = 4500
LIMIT 1;
 
-- find the total basic pay for all the employees in the organization
 
select sum(basic)
from Employee;
 
UPDATE Employee
SET Basic = 4500
WHERE dept_id = 'D1' AND Basic = 45000
LIMIT 1;
 
update Employee
set basic = 4500
where dept_id = 'D1' And basic = 45000
limit 1;
 
-- find the total pay in department d2 for all employees whose basic pay is more that 4000
 
select sum(basic)
from employee
where dept_id = 'D2' and basic>4000;
 
-- find the total pay for all the employees (basic +hra -deductins- tax) where department is 'D3'
select sum(Basic+ HRA - Deduction - TAX) as 'Total Pay'
from Employee 
where dept_id = 'D3';
 
-- find the total pay for all the employees (basic +hra -deductins) from dept d1 salary > 4500
select sum(Basic+ HRA - Deduction - TAX) as 'Total Pay'
from Employee 
where Dept_id = 'D1' and basic>4500;
 
-- average hra
select avg (HRA)
from Employee;
 
-- average pay in department d1 whose HRA > 1000
 
select avg (Basic+ HRA - Deduction - TAX)
from Employee
where dept_id = 'D1' and HRA> 1000;
 
-- find the department wise average pay of the employees
 
select Avg (Basic+ HRA - Deduction - TAX) as Avg_Pay
from Employee
group by dept_id;
 
-- find all the employees whose basic pay is greater that the average basic pay
select avg (Basic) from Employee e2;
 
select * from Employee;
 
select e1.NAME as Name, e1.Basic as Basic
from Employee e1
where Basic > (select avg (Basic) from Employee e2) ;

-- find the maximum basic pay of the employee
select name, Basic 
from employee 
where basic = (select max(Basic)
from Employee);
-- find the average , maximum and minimum basic of all the departments except department d1
select dept_id, avg(Basic+HRA-Deduction - Tax) as average_pay, MAX(Basic + HRA - Deduction - TAX) AS Maximum,
    MIN(Basic + HRA - Deduction - TAX) AS Minimum
from Employee
where dept_id <> 'D1'
group by (dept_id) ;