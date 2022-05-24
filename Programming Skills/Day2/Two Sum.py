# Leetcode: 1. Two Sum

'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#       APPROACH 1: taking list - element you r pointing, using.index method
        for i in range(len(nums)):
            # print(new_list)
            if target-nums[i] in nums[i+1:]:
                return [i,nums[i+1:].index(target-nums[i])+1]   #.index() has time complexity O(n)
#        time: O(n^2), space:O(1)
#        worst case:[1,1,1,1,1,1,2,5], target-8, getting i:O(n-1) time, for index=O(n) time
    
    
    
#       APPROACH 2:using HashMap of {element:index}, 
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i
#        time: O(n), space: O(n)
#        worst case: [1,2,2,2,2,2,5] target=6, when 5 is reached then only hashtable is checked for 1
#        https://www.youtube.com/watch?v=KLlXCFG5TnA





