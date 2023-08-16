--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS `genre`, COUNT(*) AS `Number of shows`
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY `Number of shows` DESC
