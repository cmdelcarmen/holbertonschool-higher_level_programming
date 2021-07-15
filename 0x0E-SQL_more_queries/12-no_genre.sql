-- Written by Caroline Del Carmen for Holberton Programming School
-- Script lists all shows contained in hbtn_0d_tvshows without a genre linked.
ELECT T_S.title, T_S_G.genre_id
FROM tv_show_genres AS T_S_G
RIGHT JOIN tv_shows AS T_S
ON T_S_G.show_id = T_S.id
WHERE T_S_G.genre_id IS NULL
ORDER BY T_S.title ASC,
T_S_G.genre_id;
