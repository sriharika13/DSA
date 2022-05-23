# Leetcode 263.Ugly Number
''' An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.'''

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        ugly=[2,3,5]
        for i in ugly:
            while(n%i==0 ):
                n=n/i
        return n==1
                
