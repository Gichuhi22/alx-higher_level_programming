-- change database to utf-8
-- Use hbtn_0c_0 database
-- USE hbtn_0c_0;

-- Change database to utf-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
 -- Change name to utf-8
 ALTER TABLE first_table MODIFY name VARCHAR(255) CHARACTER SET utf8mb4_unicode_ci;
 -- Change table to utf-8
  ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
