-- Written by Caroline Del Carmen for Holberton Programming School
-- Scriptcript that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT id, name FROM cities
WHERE state_id IN
(SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
