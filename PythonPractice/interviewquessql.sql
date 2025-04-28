use sqlpractice;
CREATE TABLE demo_table(
NAME varchar(30),
COLLEGE varchar(30),
EXAM_DATE DATE,
SUBJECTS varchar(30),
MARKS int);

INSERT INTO demo_table VALUES ('ROMY', 'BVCOE', 
'12-OCT-2021', 'DBMS', 90),
('ROMY', 'BVCOE', '12-OCT-2021', 'NETWORKING', 90),
('ROMY', 'BVCOE', '12-OCT-2021', 'GRAPHICS', 100),
('ROMY', 'BVCOE', '12-OCT-2021', 'CHEMISTRY', 98),
('ROMY', 'BVCOE', '12-OCT-2021', 'MATHEMATICS', 78),
('PUSHKAR', 'MSIT', '14-OCT-2021', 'NETWORKING' , 97),
('PUSHKAR', 'MSIT', '14-OCT-2021', 'GRAPHICS', 98),
('PUSHKAR', 'MSIT', '14-OCT-2021', 'CHEMISTRY', 79),
('PUSHKAR', 'MSIT', '14-OCT-2021', 'MATHEMATICS', 79),
('PUSHKAR', 'MSIT', '14-OCT-2021', 'DBMS', 79);

select * from demo_table;

create table A ( A int)
create table B ( B int)

SELECT * FROM A
SELECT * FROM B

select * from A a inner join B b on a.A=b.B
select * from A a left join B b on a.A=b.B
select * from A a right join B b on a.A=b.B
select * from A a full outer join B b on a.A=b.B
