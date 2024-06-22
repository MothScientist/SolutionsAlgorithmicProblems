SELECT
    d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON d.id = e.departmentId
WHERE
    salary IN (SELECT DISTINCT salary FROM Employee WHERE departmentId = e.departmentId ORDER BY salary DESC LIMIT 3)
ORDER BY
    d.name,
    e.salary DESC;