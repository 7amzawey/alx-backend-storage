-- Create a trigger that resets the attribue valid_email.
DELIMITER //
CREATE TRIGGER reset_email_after_change
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email
        UPDATE users
        SET valid_email = 0
    END IF;
END //
DELIMITER ;