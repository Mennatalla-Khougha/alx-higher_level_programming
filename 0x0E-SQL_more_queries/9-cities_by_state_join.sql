-- lists all cities contained in the database hbtn_0d_usa.
SELECT `cities`.`id`, `cities`.`name`, `state`.`name` 
FROM `cities` 
JOIN BY `state` 
ON `cities`.`state_id` = `state`.`id`
ORDER BY `id`;