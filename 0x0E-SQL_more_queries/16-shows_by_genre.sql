-- Written by Caroline Del Carmen for Holberton Programming School
-- Script lists all shows, and all genres linked to that show, from
-- the database hbtn_0d_tvshows
SELECT T_S.title, T_G.name FROM tv_show_genres AS T_S_G
RIGHT JOIN tv_genres AS T_G ON T_S_G.genre_id = T_G.id
RIGHT JOIN tv_shows AS T_S ON T_S_G.show_id = T_S.id
ORDER BY T_S.title ASC, T_G.name ASC;
