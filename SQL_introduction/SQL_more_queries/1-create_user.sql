-- 1. Root user
-- Creates user_0d_1 if it does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Gives user_0d_1 all privileges on the MySQL server.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
