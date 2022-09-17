# Kadane's Algorithm : Finding Maximum Subarray Sum

'''
For Example: Consider the given array A[] = [1, -2,-3, 4, -1, 2, 1]. 
Element denotes the current element at index ‘i’, MaxSum is the maximum sum obtained so far till index ‘i’, Sum denotes the current sum obtained. 

Initialize Sum to 0, MaxSum to INT_MIN 
for i = 0 
  A[i] = 1, 
  Sum = Sum + A[i] = 1 
  MaxSum = max(MaxSum,Sum) = 1 
  
for i = 1 
  A[i] = -2 
  Sum = Sum + A[i] = -1 
  MaxSum = max(MaxSum,Sum) = 1 
  
Since Sum is negative, there is no point in appending the current sum obtained to the next element, 
so Sum = 0 i.e It is better to start a new subarray from the next index. 

for i = 2 
  A[i] = -3 
  Sum = Sum + A[i] = -3 
  MaxSum = max(MaxSum,Sum) = 1 
  
Again, since Sum is negative, there is no point in appending the current sum obtained to the next element, 
so Sum = 0 i.e It is better to start a new subarray from the next index. 

for i = 3 
  A[i] = 4 
  Sum = Sum + A[i] = 4 
  MaxSum = max(MaxSum,Sum) = 4 

for i = 4 
A[i] = -1 
Sum  = Sum + A[i] = 3 
MaxSum = max(MaxSum,Sum) = 4 

Even if the element at A[i] is negative, the overall current sum is non-negative, so we retain the current sum to look for possible better options on 
appending the next elements. We have already updated the MaxSum for the subarray ending at index 3. 

for i = 5 
  A[i] = 2 
  Sum = Sum + A[i] = 5 
  MaxSum = max(MaxSum,Sum) = 5 

for i = 6 
  A[i] = 1 
  Sum  = Sum + A[i] = 6 
  MaxSum = max(MaxSum,Sum) = 6
'''

def maxSubarraySum(arr, n) :
    curr_sum=arr[0]
    max_sum=0
    for i in range(1,len(arr)):
        curr_sum= curr_sum + arr[i]
        if curr_sum<0:
            curr_sum=0
        else:
            max_sum= max(max_sum, curr_sum)

    return max_sum
# T= O(n)
# S= O(1)

