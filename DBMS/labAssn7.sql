create table Library (book_id int primary key auto_increment, book_name varchar(50), book_author varchar(50));
insert into Library values(101, "physics made easy", "hc verma");
insert into Library(book_name,book_author) values("icse chemistry", "viraf dalal");
insert into Library(book_name,book_author) values("icse biology", "anita prasad");
insert into Library(book_name,book_author) values("harry potter", "jk rowling");

create table Library_audit(bookid int , bookname varchar(50), bookauthor varchar(50));

delimiter $$
create trigger after_book_update after update on Library
for each row 
begin
    declare bkid int;
    declare bkname varchar(50);
    declare bkauthor varchar(50);
    set bkid = new.book_id;
    set bkname = new.book_name;
    set bkauthor = new.book_author;
    insert into Library_audit values(bkid,bkname,bkauthor);
end;
$$
delimiter ;

update Library set book_name="dsa",book_author="bv sharma" where book_id=103;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from Library;
+---------+-------------------+-------------+
| book_id | book_name         | book_author |
+---------+-------------------+-------------+
|     101 | physics made easy | hc verma    |
|     102 | icse chemistry    | viraf dalal |
|     103 | dsa               | bv sharma   |
|     104 | harry potter      | jk rowling  |
+---------+-------------------+-------------+
4 rows in set (0.00 sec)

mysql> select * from Library_audit;
+--------+----------+------------+
| bookid | bookname | bookauthor |
+--------+----------+------------+
|    103 | dsa      | bv sharma  |
+--------+----------+------------+
1 row in set (0.00 sec)
mysql> delimiter ##
mysql> create trigger after_delete_book after delete on Library 
    -> for each row
    -> begin
    ->     declare bkid int;
    ->     declare bkname varchar(50);
    ->     declare bkauthor varchar(50);
    ->     set bkid = old.book_id;
    ->     set bkname = old.book_name;
    ->     set bkauthor = old.book_author;
    ->     insert into Library_audit values(bkid, bkname, bkauthor);
    -> end;
    -> ##
Query OK, 0 rows affected (0.01 sec)

mysql> delimiter ;

delete from Library where book_name="harry potter";
Query OK, 1 row affected (0.00 sec)

mysql> select * from Library;
+---------+-------------------+-------------+
| book_id | book_name         | book_author |
+---------+-------------------+-------------+
|     101 | physics made easy | hc verma    |
|     102 | icse chemistry    | viraf dalal |
|     103 | dsa               | bv sharma   |
+---------+-------------------+-------------+
3 rows in set (0.00 sec)

mysql> select * from Library_audit;
+--------+--------------+------------+
| bookid | bookname     | bookauthor |
+--------+--------------+------------+
|    103 | dsa          | bv sharma  |
|    104 | harry potter | jk rowling |
+--------+--------------+------------+
2 rows in set (0.00 sec)




