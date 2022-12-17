create table old_Emp(OEmp_id int, OEmp_name varchar(25), OEmp_dept varchar(25));
insert into old_Emp values(1,"Sanika","Engg");
insert into old_Emp values(2,"Sharvi","Prod");
insert into old_Emp values(3,"Ruturaj","QA");
insert into old_Emp values(4,"Atharv","QA");
insert into old_Emp values(5,"Dinesh","Engg");
insert into old_Emp values(6,"Tanmay","Prod");

create table new_Emp(NEmp_id int, NEmp_name varchar(25), NEmp_dept varchar(25));
insert into new_Emp values(2,"Sharvi","Prod");

select * from old_Emp;
select * from new_Emp;

delimiter @@
create procedure add_Emp(in Emp_id int)
begin
    declare Emp_id2 int;
    declare exitflag boolean default false;

    declare curEmp cursor for select OEmp_id from old_Emp where OEmp_id > Emp_id;
    declare continue handler for not found set exitflag = true;

    open curEmp;
    loop1: loop
    fetch curEmp into Emp_id2;
        if not exists(select * from new_Emp where NEmp_id=Emp_id2) then
        insert into new_Emp select * from old_Emp where OEmp_id=Emp_id2;
        end if;
        if exitflag then 
            close curEmp;
            leave loop1;
        end if;
    end loop loop1;
end
@@
delimiter ;


mysql> select * from old_Emp;
+---------+-----------+-----------+
| OEmp_id | OEmp_name | OEmp_dept |
+---------+-----------+-----------+
|       1 | Sanika    | Engg      |
|       2 | Sharvi    | Prod      |
|       3 | Ruturaj   | QA        |
|       4 | Atharv    | QA        |
|       5 | Dinesh    | Engg      |
|       6 | Tanmay    | Prod      |
+---------+-----------+-----------+
6 rows in set (0.00 sec)

mysql> select * from new_Emp;
+---------+-----------+-----------+
| NEmp_id | NEmp_name | NEmp_dept |
+---------+-----------+-----------+
|       2 | Sharvi    | Prod      |
+---------+-----------+-----------+
1 row in set (0.00 sec)

call add_Emp(2);
Query OK, 0 rows affected (0.01 sec)

mysql> select * from new_Emp;
+---------+-----------+-----------+
| NEmp_id | NEmp_name | NEmp_dept |
+---------+-----------+-----------+
|       2 | Sharvi    | Prod      |
|       3 | Ruturaj   | QA        |
|       4 | Atharv    | QA        |
|       5 | Dinesh    | Engg      |
|       6 | Tanmay    | Prod      |
+---------+-----------+-----------+
5 rows in set (0.00 sec)

