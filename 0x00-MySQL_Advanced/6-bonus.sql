-- create a procedure
DELIMITER //
CREATE PROCEDURE 
AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
       	INSERT INTO corrections(user_id, project_id, score) 
	values(user_id, (select id from projects WHERE projects.name = project_name), score);

END //
DELIMITER ;
