-- lists all cities contained in the database hbtn_0d_usa.
SELECT `id`, `name`, `name` 
FROM `cities` JOIN BY `state` ON `id`
ORDER BY `id`;