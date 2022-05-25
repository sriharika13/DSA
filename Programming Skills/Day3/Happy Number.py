# Leetcode 202.Happy Number

'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.'''

class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

# APPROACH: Loop example: A-> B -> C -> D going back to A or can be partial like going to B.
''' If we use a set which stores only a unique element can save us from storing same numbers again. 
Before inserting a number in set, check if it exist in set before or if the number is 1 
If we encounter number is already present ins set, just return false tht original number of not happy

Time: O(number of digits in num * number of elements in set )
Space: O( number of elements in set)
'''

                          
                        
