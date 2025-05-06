/* Day 43 - May 4, 2025
 * 182. Duplicate Emails
 * https://leetcode.com/problems/duplicate-emails/
 */

--Solution
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;