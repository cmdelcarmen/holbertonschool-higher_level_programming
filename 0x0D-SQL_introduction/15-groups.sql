-- Written by Caroline Del Carmen for Holberton Programming School
-- Script lists the number of records with the same score in the table
-- 'second_table' of the database hbtn_0c_0 in MySQL srever
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
