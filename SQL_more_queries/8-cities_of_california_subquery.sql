-- 8-cities_of_california_subquery.sql
-- Brad Brown

SELECT id, name 
FROM cities 
WHERE state_id = (
	SELECT id FROM states WHERE name = 'California'
	);
