create table Borrower(rollno int, name varchar(25), issuedate date, bookname varchar(50), status varchar(25));
create table Fine(Rollno int, Date date, Amt int);

alter table Borrower modify rollno int primary key;
alter table Fine add foreign key(Rollno) references Borrower(rollno);

insert into Borrower values(31135,"Sanika","2022-10-13","ikigai","issued");
insert into Borrower values(31124,"Sharvi","2022-10-20","richdadpoordad","issued");
insert into Borrower values(31126,"Rohan","2022-10-01","harry potter","issued");
insert into Borrower values(31129,"Ruturaj","2022-9-25","dsa basics","issued");
insert into Borrower values(31143,"Tanmay","2022-11-10","mechanics","issued");
insert into Borrower values(31105,"Atharv","2022-10-30","oop in python","issued");
insert into Borrower values(31153,"Dinesh","2022-10-30","oop in python","issued");
insert into Borrower values(31159,"Mrunmay","2022-10-29","oop in python","issued");

mysql> select * from Borrower;
+--------+---------+------------+----------------+--------+
| rollno | name    | issuedate  | bookname       | status |
+--------+---------+------------+----------------+--------+
|  31105 | Atharv  | 2022-10-30 | oop in python  | issued |
|  31124 | Sharvi  | 2022-10-20 | richdadpoordad | issued |
|  31126 | Rohan   | 2022-10-01 | harry potter   | issued |
|  31129 | Ruturaj | 2022-09-25 | dsa basics     | issued |
|  31135 | Sanika  | 2022-10-13 | ikigai         | issued |
|  31143 | Tanmay  | 2022-11-10 | mechanics      | issued |
|  31153 | Dinesh  | 2022-10-30 | oop in python  | issued |
|  31159 | Mrunmay | 2022-10-29 | oop in python  | issued |
+--------+---------+------------+----------------+--------+

delimiter ##
create procedure calc_fine(in roll_No int, in book_Name varchar(50))
begin
      declare days int;  
      declare pre_status varchar(50);

      declare exit handler for SQLSTATE '43250' 
      begin
            select 'Book was already returned' as Exception;
      end;
      select status into pre_status from Borrower where bookname=book_Name and rollno=roll_No;
      if (pre_status = "returned") then SIGNAL SQLSTATE '43250';
      end if;

      select DATEDIFF(CURRENT_DATE,issuedate) into days from Borrower where rollno=roll_No and bookname=book_Name;
      if days > 15 and days < 30 then
      insert into Fine values(roll_No,CURRENT_DATE,(days-15)*5);
      elseif days >=30 then
      insert into Fine values(roll_No,CURRENT_DATE,(days-30)*50 + 15*5);
      end if;
      update Borrower set status="returned" where rollno=roll_No and bookname=book_Name;
end
##
delimiter ;
call calc_fine(31135,"ikigai");
call calc_fine(31124,"richdadpoordad");
call calc_fine(31105,"oop in python");
call calc_fine(31159,"oop in python");

mysql> select * from Fine;
+--------+------------+------+
| Rollno | Date       | Amt  |
+--------+------------+------+
|  31135 | 2022-11-13 |  125 |
|  31124 | 2022-11-13 |   45 |
|  31159 | 2022-11-14 |    5 |
+--------+------------+------+
3 rows in set (0.00 sec)

mysql> select * from Borrower;
+--------+---------+------------+----------------+----------+
| rollno | name    | issuedate  | bookname       | status   |
+--------+---------+------------+----------------+----------+
|  31105 | Atharv  | 2022-10-30 | oop in python  | returned |
|  31124 | Sharvi  | 2022-10-20 | richdadpoordad | returned |
|  31126 | Rohan   | 2022-10-01 | harry potter   | issued   |
|  31129 | Ruturaj | 2022-09-25 | dsa basics     | issued   |
|  31135 | Sanika  | 2022-10-13 | ikigai         | returned |
|  31143 | Tanmay  | 2022-11-10 | mechanics      | issued   |
|  31153 | Dinesh  | 2022-10-30 | oop in python  | returned |
|  31159 | Mrunmay | 2022-10-29 | oop in python  | issued   |
+--------+---------+------------+----------------+----------+
8 rows in set (0.00 sec)

