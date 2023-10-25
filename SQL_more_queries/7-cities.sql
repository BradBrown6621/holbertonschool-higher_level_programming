-- 7-cities.sql
-- Brad Brown

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
	name VARCHAR(256),
	state_id INT NOT NULL,

	FOREIGN KEY (state_id) REFERENCES states(id)
	);
