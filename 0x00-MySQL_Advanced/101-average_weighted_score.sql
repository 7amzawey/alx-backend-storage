DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    DECLARE average_score FLOAT;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the total weighted score and total weight for the current user
        SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
        INTO total_weighted_score, total_weight
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- Calculate the average weighted score
        SET average_score = total_weighted_score / total_weight;

        -- Update the user's average score
        UPDATE users
        SET average_score = average_score
        WHERE id = user_id;
    END LOOP;

    CLOSE user_cursor;
END $$

DELIMITER ;
