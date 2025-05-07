/* Day 44 - May 6, 2025
 * 183. Customers Who Never Order
 * https://leetcode.com/problems/customers-who-never-order/
 */

--Solution
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;