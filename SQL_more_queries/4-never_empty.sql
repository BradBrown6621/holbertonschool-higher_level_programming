-- 4-never_empty.sql
-- Brad Brown

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
	);
