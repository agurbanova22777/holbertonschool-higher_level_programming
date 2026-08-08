-- 6. States table
-- Creates the hbtn_0d_usa database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates the states table if it does not already exist.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
