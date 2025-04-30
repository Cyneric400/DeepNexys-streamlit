UPDATE Documents SET user_id = 1 WHERE Documents.contents LIKE '%flag%';
SELECT * FROM Documents;

DELETE FROM Documents WHERE file_id >= 1;