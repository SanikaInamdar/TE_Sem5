create table Area (radius int, areas double);

delimiter ##
create procedure calc_area()
begin
    declare rad int default 5;
    while rad<10 do
    insert into Area values(rad,3.14*rad*rad);
    set rad = rad + 1;
    end while;
end
##
delimiter ;

mysql> select * from Area;
+--------+--------+
| radius | areas  |
+--------+--------+
|      5 |   78.5 |
|      6 | 113.04 |
|      7 | 153.86 |
|      8 | 200.96 |
|      9 | 254.34 |
+--------+--------+
5 rows in set (0.02 sec)


procedure with out parameter

CREATE PROCEDURE TOTAL_PENALTIES_PLAYER
   (IN P_PLAYERNO INTEGER,
    OUT TOTAL_PENALTIES DECIMAL(8,2))
BEGIN
   SELECT SUM(AMOUNT)
   INTO   TOTAL_PENALTIES
   FROM   PENALTIES
   WHERE  PLAYERNO = P_PLAYERNO;
END
CALL TOTAL_PENALTIES_PLAYER (27, @TOTAL)
SELECT @TOTAL
