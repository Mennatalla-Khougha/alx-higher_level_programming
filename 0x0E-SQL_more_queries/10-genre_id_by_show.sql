-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT `title`, `genre_id`
FROM `tv_shows`
ORDER BY `title`, `genre_id`;