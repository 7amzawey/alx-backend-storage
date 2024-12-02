-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name, valid_email) VALUES ("email0@test.com", "Test 0", 1);
INSERT INTO users (email, name, valid_email) VALUES ("email1@test.com", "Test 1", 0);
INSERT INTO users (email, name, valid_email) VALUES ("email2@test.com", "Test 2", 1);
INSERT INTO users (email, name, valid_email) VALUES ("email3@test.com", "Test 3", 0);
