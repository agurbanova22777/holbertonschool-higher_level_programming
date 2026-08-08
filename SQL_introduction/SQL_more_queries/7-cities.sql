-- 7. Cities table
-- Creates the hbtn_0d_usa database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates the cities table with a foreign key to states.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
