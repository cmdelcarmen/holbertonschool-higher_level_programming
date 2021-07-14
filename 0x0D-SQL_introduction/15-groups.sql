-- Written by Caroline Del Carmen for Holberton Programming School
-- Script lists the number of records with the same score in the table
-- 'second_table' of the database hbtn_0c_0 in MySQL srever
SELECT score, COUNT(*) AS numer FROM second_table
GROUP BY sore ORDER BY number DESC;
