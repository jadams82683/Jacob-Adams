USE twitter;

INSERT INTO users (first_name, last_name, handle, birthday)
VALUES ("Sarah", "Burlingham", "sbham", "1986-03-12");

INSERT INTO users (first_name, last_name, handle, birthday)
VALUES ("Salem", "Burlingham", "fluffynugget", "2012-10-31");

UPDATE users SET 
handle = "MisterXYZ"
WHERE id= 11;

DELETE FROM users WHERE id = 21;
DELETE FROM users WHERE id = 22;

SELECT * from users












