-- Update one email of a valid email
SELECT * FROM users;

UPDATE users SET email = "email0+new@test.com" WHERE email = "email0@test.com";

SELECT "--";
SELECT * FROM users;

UPDATE users SET name = "New name" WHERE email = "email0@test.com";

SELECT "--";
SELECT * FROM users;
