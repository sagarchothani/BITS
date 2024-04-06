show databases;
 
 
use mysql; 
show tables;
 
desc db;
 
create table persons
(person_ID int,
last_name varchar(255),
first_name varchar(255),
address varchar(255),
city varchar(255));
 
create table customers
( ID INT Not NULL,
Name Varchar(255) Not Null,
Age Int Not Null,
Address char(25),
Salary decimal(18,2),
Primary Key (ID) );
 
 
desc customers;
 
Alter table customers
Drop primary key;
 
Desc customers;
 
Alter table customers
ADD Primary key (ID, Name);
 
Insert into customers (ID, Name, Age, Address, Salary) 
Values (123, 'Amit', 32, 'BITS Pilani', 20000000);
 
select * from Customers;
 
 
desc customers;
 
select * from customers;
 
create table book(
ISBN INT,
Title Varchar(35),
Author_name Varchar(35),
Publisher_name Varchar (40),
Date_of_Publication Date,
Price Int);
 
 
Insert into book (ISBN, Title, Author_name, Publisher_name, Date_of_Publication, Price) Values 
(1, 'Software engineering','Pressman', 'TMH', makedate(2007,1), 50);
 
INSERT INTO book (ISBN, Title, Author_name, Publisher_name, Date_of_Publication, Price) VALUES 
(2, 'DBMS', 'Korth', 'TMH', '1997-01-01', 45),
(3, 'SQL', 'Local', 'Person', '1997-01-01', 25),
(4, 'Algorithm', 'Cormen', 'Person', '2001-01-01', 75),
(5, 'Algorithm', 'Local', 'TMH', '2010-01-01', 45),
(6, 'SQL', 'James', 'TMH', '2017-01-01', 56);





-- Get the title, author name and publisher of all books published in 1997 and the price is greater than 25
select* from book;

select Title, Author_name, Publisher_name
from book
where Date_of_Publication >='1997-01-01' and Date_of_Publication<='1997-12-31' and Price > 25;
-- where Date_of_Publication >='1997-01-01' and Date_of_Publication<='1997-12-31' and Price >= 25;

-- get the title, author and publisher name of all the books. Published in year 1993,1996 and 1998


select Title, Author_name, Publisher_name
from book
where Year(Date_of_Publication) not in (1993,1996,1998);

select * 
from book
where price>=10 and price<=25;

select * 
from book
where price>=10 and price<=25;