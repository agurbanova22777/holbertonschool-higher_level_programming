-- 8. Cities of California
-- Lists cities belonging to California.
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;
