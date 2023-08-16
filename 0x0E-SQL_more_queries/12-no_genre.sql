-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT `tv`.`title`, `gen`.`genre_id`
FROM `tv_shows` AS `tv`
LEFT JOIN `tv_show_genres` AS `gen`
ON `tv`.`id` = `gen`.`show_id`
WHERE `gen`.`genre_id` IS NULL
ORDER BY `tv`.`title`;