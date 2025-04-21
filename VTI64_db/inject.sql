UPDATE Files SET user_id = 1 WHERE user_id = 0;

SELECT * FROM Files;

UPDATE Files SET contents='flag{congratulations}' WHERE file_id = 0

DELETE FROM Files WHERE file_id >= 2;