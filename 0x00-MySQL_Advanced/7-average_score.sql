-- calculate the average student score
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score FLOAT;

    -- Calculate the average score for the user
    SELECT AVG(score) INTO average_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Update the user's average score
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END //
DELIMITER ;
