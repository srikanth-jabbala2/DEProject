use sqlpractice;

create table depttrans(
    Id int primary key,
    Name varchar(50),
    DeptId int,
)

-- DeptId is int, change it to varchar(50)
alter table depttrans
alter column DeptId varchar(50);
-- DeptId is int, change it to varchar(50)

INSERT  (1, "a", "aa"),
    (1, "s", "ss"),
    (2, "d", "dd"),
    (2, "d", "dd"),
    (3, "h", "gg"),
    (4, "j", "h"),
    (5, "k", "jj"),
    (5, "k", "jj"),
    (7, "o", "ww"),
    (8, "u", "qq"),
    (9, "t", "aa")

INSERT INTO depttrans (Id, Name, DeptId) VALUES
(1, 'a', 'aa'),
(10, 's', 'ss'),
(2, 'd', 'dd'),
(2, 'd', 'dd'),
(3, 'h', 'gg'),
(4, 'j', 'h'),
(5, 'k', 'jj'),
(5, 'k', 'jj'),
(7, 'o', 'ww'),
(8, 'u', 'qq'),
(9, 't', 'aa');

SELECT * FROM depttrans ORDER BY id ASC;

--remove duplicate rows using cte
WITH CTE AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY Id, Name, DeptId ORDER BY Id) AS rn
    FROM depttrans
)
DELETE FROM CTE WHERE rn > 1;


DELETE FROM depttrans
WHERE Id IN (SELECT Id FROM depttrans GROUP BY Id HAVING COUNT(*) > 1);

ALTER TABLE depttrans 
DROP CONSTRAINT PK__depttran__3214EC0784F935E8;

SELECT * from INFORMATION_SCHEMA.table_constraints where table_name = 'depttrans';

