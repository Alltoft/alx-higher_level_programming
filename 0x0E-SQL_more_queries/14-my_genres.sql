-- a script that uses the hbtn_0d_tvshows database to lists all genres
-- of the show Dexter.
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.show_id
WHERE tv_show_genres.title = "DEXTER"
ORDER BY tv_genres.name;
