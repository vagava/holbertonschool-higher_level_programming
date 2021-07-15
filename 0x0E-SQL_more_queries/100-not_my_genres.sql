-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN(
	SELECT tv_show_genres.genre_id
	FROM (tv_shows
	JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id)
	WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name ASC;




SELECT *
FROM (( tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id)
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
WHERE tv_show_genres.show_id IS NULL OR tv_shows.id IS NULL;
