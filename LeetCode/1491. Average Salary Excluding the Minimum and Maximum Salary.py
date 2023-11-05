# 1491. Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary) / len(salary)
