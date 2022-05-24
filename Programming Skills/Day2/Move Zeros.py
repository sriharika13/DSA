# Leetcode 283. Move Zeros
'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.'''

 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
#     APPROACH 1: using space and maintaining zeros_cnt:
        numZeros=0
        for i in range(len(nums)):
            if nums[i]==0:
                numZeros+=1
        ans=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                ans.append(nums[i])
        while(numZeros>0):
            ans.append(0)
            numZeros-=1
        for i in range(len(nums)):
            nums[i]=ans[i]
#             Time: O(n), Space: O(n)



# APPROACH 2: 2-pointer approach and optimising space:
 	    lastNonZeroFoundAt=0
 	    #If the current element is not 0, then we need to
 	    #append it just in front of last non 0 element we found.
 	    for i in range(len(nums)):
 	        if nums[i]!=0:
 	            nums[lastNonZeroFoundAt]=nums[i] 
 	            lastNonZeroFoundAt+=1
 	    #After we have finished processing new elements,
 	    #all the non-zero elements are already at beginning of array.
 	    #We just need to fill remaining array with 0's.
 	    for i in range(lastNonZeroFoundAt, len(nums)):
 	        nums[i]=0
#     time: O(n), space:O(1)
# worst case: [0,0,0,0,0,0,0,0,1] for loop i goes O(n) and for zeros o(n-1)
            
    
    
# APPROACH 3: swapping non_zero elements with zeros
        def swap(a,b):
            temp=b
            b=a
            a=temp
        for i in range(len(nums)):
            lastNonZeroFoundAt =0
            if nums[i]!=0:
                swap(nums[lastNonZeroFoundAt], nums[i])
                lastNonZeroFoundAt+=1
#          time:O(n), space: O(1)
# The total operations (array writes) that code does is Number of non-0 elements.
# This gives us a much better best-case (when most of the elements are 0) complexity than last solution.
# worst case: [1,2,3,4,4,5,6] all non-zeros 
#                 https://leetcode.com/problems/move-zeroes/solution/
            
 
 
 
 
                
