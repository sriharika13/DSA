#Leetcode 1491.Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary: List[int]) -> float:
        minn=min(salary)
        maxx= max(salary)
        print(minn)
        print(maxx)
        a=(sum(salary)-(minn+maxx))/(len(salary)-2)
        return a
