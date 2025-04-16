DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Files;

CREATE TABLE User(
    id INT,
    name VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE Files(
    user_id INT,
    contents TEXT,
    filepath TEXT,
    FOREIGN KEY (user_id) REFERENCES User
);