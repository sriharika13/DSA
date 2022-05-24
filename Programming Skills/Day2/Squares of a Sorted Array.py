# Leetcode 977.Squares of a Sorted Array

'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        low=0
        high=len(nums)-1
        while(low<=high):
            if abs(nums[low])<=abs(nums[high]):
                ans.append(nums[high]**2)
                high-=1
            else: 
                ans.append(nums[low]**2)
                low+=1
        return ans[::-1]
#       time: O(n), space: O(n)
