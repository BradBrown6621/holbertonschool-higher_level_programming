-- 9-cities_by_state_join.sql
-- Brad Brown

SELECT cities.id, cities.name
FROM cities
JOIN states
ON states.id = cities.id
ORDER BY cities.id;
