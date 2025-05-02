/* Day 42 - May 2, 2025
 * 181. Employees Earning More Than Their Managers
 * https://leetcode.com/problems/employees-earning-more-than-their-managers/
 */

--Solution
SELECT E1.name AS Employee
FROM Employee E1
JOIN Employee E2
ON E1.managerId = E2.id
WHERE E1.salary > E2.salary;