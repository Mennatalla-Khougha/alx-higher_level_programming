--  lists all shows, and all genres linked to that show
SELECT `tv`.`title` , `gen`.`name`
FROM `tv_shows` AS `tv`
LEFT JOIN `tv_show_genres` as `tv_s_g` 
ON `tv_s_g`.`show_id` = `tv`.`id`
LEFT JOIN `tv_genres` AS `gen`
ON `tv_s_g`.`genre_id` = `gen`.`id`
ORDER BY `tv`.`title`, `gen`.`name`;