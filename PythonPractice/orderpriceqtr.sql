use sqlpractice;

create table orders(
    order_id  bigint primary key,
    p_name    varchar(50),
    price    decimal(10,2),
    orderdate date
)

INSERT INTO orders (order_id, p_name, price, orderdate) VALUES
(1, 'Wireless Mouse',     25.99, '2025-01-15'),
(2, 'Laptop Stand',       34.50, '2025-02-10'),
(3, 'USB-C Cable',        10.99, '2025-03-20'),
(4, 'Bluetooth Speaker',  45.00, '2025-04-05'),
(5, 'Webcam',             60.00, '2025-05-12'),
(6, 'Mechanical Keyboard',89.99, '2025-06-22'),
(7, 'External SSD',      120.50, '2025-07-18'),
(8, 'Monitor',           199.99, '2025-08-03'),
(9, 'Smartwatch',        150.00, '2025-09-29'),
(10, 'Noise Cancelling Headphones', 299.99, '2025-10-11'),
(11, 'Gaming Chair',      249.00, '2025-11-23'),
(12, 'Tablet',            399.99, '2025-12-30');

SELECT * FROM orders;


SELECT
    case WHEN MONTH(orderdate)>=1 AND month(orderdate)<=3 then'q1' 
       WHEN MONTH(orderdate)>3 and month(orderdate)<=6 then 'q2' 
       WHEN month(orderdate)>6 and month(orderdate)<=9 then 'q3'
       WHEN month(orderdate)>9 and month(orderdate)<=12 then 'q4' 
        end as qtr
FROM orders;

WITH QRT AS(
SELECT PRICE,
    case WHEN MONTH(orderdate)>=1 AND month(orderdate)<=3 then'q1' 
       WHEN MONTH(orderdate)>3 and month(orderdate)<=6 then 'q2' 
       WHEN month(orderdate)>6 and month(orderdate)<=9 then 'q3'
       WHEN month(orderdate)>9 and month(orderdate)<=12 then 'q4' 
        end as qtr
FROM orderS
) 
SELECT SUM(PRICE) as total,QTR FROM QRT GROUP BY QTR

use sqlpractice;
DROP TABLE IF EXISTS TRANSACTIONS;

CREATE TABLE TRANSACTIONS(
    TRASACTION_ID BIGINT PRIMARY KEY,
    TRANSACTION_DATE DATE,
    AMOUNT DECIMAL(10,2),
    TRANSACTION_TYPE VARCHAR(50)
)

INSERT INTO TRANSACTIONS (TRASACTION_ID, TRANSACTION_DATE, AMOUNT, TRANSACTION_TYPE) VALUES
(1, '2024-02-19T00:00:00.0000000', 100, 'Credit'),
(2, '2024-02-19T00:00:00.0000000', 200, 'Debit'),
(3, '2024-02-18T00:00:00.0000000', 300, 'Credit'),
(4, '2024-02-18T00:00:00.0000000', 400, 'Debit'),
(5, '2024-02-18T00:00:00.0000000', 400, 'Credit'),
(6, '2024-02-18T00:00:00.0000000', 1800, 'Credit')



SELECT * FROM TRANSACTIONS;


select 
    sum(case 
        when TRANSACTION_TYPE='Credit' then +amount
        when TRANSACTION_TYPE='Debit' then -amount
        else 0 end) as total_amount,
    cast(transaction_date as date) as transaction_date
    from 
    transactions
    group by cast(transaction_date as date)
    order by transaction_date desc;