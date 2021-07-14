-- Written by Caroline Del Carmen for Holberton Programming School
-- Script that lists all records of the 'second_table' of the database
-- 'hbtn_0c_0' in my MySQL
SELECT score, name FROM second_table WHERE name != ""
ORDER BY score DESC;
