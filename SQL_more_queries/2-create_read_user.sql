-- 2. Read user
-- Creates the database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates user_0d_2 if it does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Gives user_0d_2 only SELECT privilege on hbtn_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
