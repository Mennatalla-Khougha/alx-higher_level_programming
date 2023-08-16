--  lists all Comedy shows in the database hbtn_0d_tvshows
SELECT `tv`.`title`
FROM `tv_shows` AS `tv`
JOIN `tv_show_genres` AS `tv_s_g`
ON `tv`.`id` = `tv_s_g`.`show_id`
JOIN `tv_genres` AS `gen`
ON `gen`.`id` = `tv_s_g`.`genre_id`
WHERE `gen`.`name` = "Comedy"
ORDER BY `tv`.`title`;