create database sqlpractice;
use sqlpractice;
if object_id('employee', 'U') is not null
    drop table employee;

create table employee(
    emp_id int primary key,
    emp_name varchar(50),
    emp_salary decimal(10,2),
    emp_department varchar(50)
);
insert into employee values(1,'John Doe',50000.00,'HR');
insert into employee values(2,'Jane Smith',60000.00,'Finance');
insert into employee values(3,'Sam Brown',55000.00,'IT');
insert into employee values(4,'Lisa White',70000.00,'Marketing');

select * from employee;
SELECT * FROM employee WHERE emp_salary > 55000;
SELECT * FROM employee WHERE emp_department = 'IT';

create TABLE dept(
    dept_id int primary key,
    dept_name varchar(50),
    dept_location varchar(50)
);
insert into dept values(1,'HR','New York');
insert into dept values(2,'Finance','Los Angeles');
insert into dept values(3,'IT','San Francisco');
insert into dept values(4,'Marketing','Chicago');
insert into dept values(5,'Sales','Seattle');
insert into dept values(6,'Operations','Boston');
SELECT * FROM dept;