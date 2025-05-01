/* Day 41 - April 30, 2025
 * 175. Combine Two Tables
 * https://leetcode.com/problems/combine-two-tables/
 */

--Solution
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
    ON p.personId = a.personId;