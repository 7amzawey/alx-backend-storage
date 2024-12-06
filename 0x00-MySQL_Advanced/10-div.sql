-- Create a function on MySQL
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
       RETURNS FLOAT
       RETURN (SELECT IF(b=0,0,a/b));
$$