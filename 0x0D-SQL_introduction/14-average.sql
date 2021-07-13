-- computes the score average of all records
-- in the table second_table
ALTER TABLE second_table ADD average;
SELECT AVG(score) AS [score_average]
FROM second_table;
INSERT INTO `second_table` (average) VALUES ([score_average]);
