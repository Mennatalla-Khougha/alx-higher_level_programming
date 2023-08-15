-- converts hbtn_0c_0 database to UTF8 (utf8mb4)
USE `hbtc_0c_0`
ALTER table `first_table` 
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8_unicode_ci;