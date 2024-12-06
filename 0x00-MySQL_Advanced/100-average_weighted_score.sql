-- creates a stored procedure the computes the average score.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score FLOAT;
    DECLARE total_weight INT;
    DECLARE total_weighted_score FLOAT;

    SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
    INTO total_weighted_score, total_weight
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    AND corrections.user_id = user_id;

    update users
    SET average_score = total_weighted_score / total_weight
    WHERE id = user_id;

END $$
DELIMITER ;
