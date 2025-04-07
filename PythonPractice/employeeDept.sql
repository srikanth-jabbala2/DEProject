-- emp_id	emp_name	department_id	salary
-- 1	Alice	101	60000
-- 2	Bob	102	75000
-- 3	Charlie	101	80000
-- 4	David	103	72000
-- 5	Alice	102	60000
-- 6	Eve	NULL	65000

-- department_id	department_name
-- 101	HR
-- 102	IT
-- 103	Finance

create table employees( emp_id int, emp_name varchar(10), department_id int, salary int );
insert into employees values(1, 'Alice', 101, 60000);
insert into employees values(2, 'Bob', 102, 75000);
insert into employees values(3, 'Charlie', 101, 80000);
insert into employees values(4, 'David', 103, 72000);
insert into employees values(5, 'Alice', 102, 60000);
insert into employees values(6, 'Eve',NULL,65000);

SELECT * FROM employees

create table Department( department_id int, department_name varchar(10));
insert into Department values(101, 'HR');
insert into Department values(102, 'IT');
insert into Department values(103, 'Finance');

select * from Department;

select avg(a.salary) as avg_Sal , b.department_name from employees a join Department b on a.department_id=b.department_id
group by b.department_name