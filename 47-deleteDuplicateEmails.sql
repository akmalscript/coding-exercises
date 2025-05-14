/* Day 47 - May 12, 2025
 * 196. Delete Duplicate Emails
 * https://leetcode.com/problems/delete-duplicate-emails/
 */

-- Solution
DELETE FROM Person
WHERE id NOT IN (
    SELECT id FROM (
        SELECT MIN(id) AS id
        FROM Person
        GROUP BY email
    ) AS temp
);