CREATE TABLE Stud_Marks(RollNo INT PRIMARY KEY, Sname VARCHAR(20), Total_Marks INT );
Query OK, 0 rows affected (0.05 sec)

mysql> CREATE TABLE Result(RollNo INT REFERENCES Stud_Marks(RollNo), Sname VARCHAR(20), Marks INT, Grade VARCHAR(20) );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO Stud_Marks VALUES
    -> (1, 'Vidyut', 995),
    -> (2, 'Pratap', 828),
    -> (3, 'Kailash', 945),
    -> (4, 'Mukund', 1500),
    -> (5, 'Girish', 900),
    -> (6, 'Neeraj', 850),
    -> (7, 'Prashant', 800),
    -> (8, 'Raj', 899),
    -> (9, 'Hari', 1300),
    -> (10, 'Aditya', 920);
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> select * from Stud_marks;
+--------+----------+-------------+
| RollNo | Sname    | Total_Marks |
+--------+----------+-------------+
|      1 | Vidyut   |         995 |
|      2 | Pratap   |         828 |
|      3 | Kailash  |         945 |
|      4 | Mukund   |        1500 |
|      5 | Girish   |         900 |
|      6 | Neeraj   |         850 |
|      7 | Prashant |         800 |
|      8 | Raj      |         899 |
|      9 | Hari     |        1300 |
|     10 | Aditya   |         920 |
+--------+----------+-------------+
10 rows in set (0.01 sec)

mysql> delimiter //
mysql> create function fun_Grade1(Student_Marks INT)
    -> returns varchar(20)
    -> DETERMINISTIC
    -> BEGIN
    -> 
    -> Declare Student_Grade varchar(20) default 'PASS';
    -> 
    -> if Student_Marks >= 990 then
    -> set Student_Grade = 'Distinction';
    -> 
    -> elseif Student_Marks >= 900 then
    -> set Student_Grade = 'First Class';
    -> 
    -> elseif Student_Marks >= 825 then
    -> set Student_Grade = 'Higher Second Class';
    -> 
    -> end if;
    -> 
    -> return Student_Grade;
    -> 
    -> END //
Query OK, 0 rows affected (0.01 sec)

mysql> 
mysql> delimiter ;
mysql> SELECT RollNo, Sname, Total_Marks, fun_Grade1(Total_Marks) AS GRADE  FROM Stud_marks ORDER BY RollNo;
+--------+----------+-------------+---------------------+
| RollNo | Sname    | Total_Marks | GRADE               |
+--------+----------+-------------+---------------------+
|      1 | Vidyut   |         995 | Distinction         |
|      2 | Pratap   |         828 | Higher Second Class |
|      3 | Kailash  |         945 | First Class         |
|      4 | Mukund   |        1500 | Distinction         |
|      5 | Girish   |         900 | First Class         |
|      6 | Neeraj   |         850 | Higher Second Class |
|      7 | Prashant |         800 | PASS                |
|      8 | Raj      |         899 | Higher Second Class |
|      9 | Hari     |        1300 | Distinction         |
|     10 | Aditya   |         920 | First Class         |
+--------+----------+-------------+---------------------+
10 rows in set (0.00 sec)

mysql> 
