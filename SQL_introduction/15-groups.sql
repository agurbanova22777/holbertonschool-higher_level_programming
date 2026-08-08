-- 15. Number by score
-- Counts records for each score and sorts by count
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
