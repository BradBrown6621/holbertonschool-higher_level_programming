-- 5-unique_id.sql
-- Brad Brown

CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
