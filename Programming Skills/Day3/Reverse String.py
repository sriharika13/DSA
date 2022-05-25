# LeetCode 344.Reverse String

'''Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s.reverse()     #time: O(n)
        
        head=0
        tail=len(s)-1
        while(head<tail):
            s[head], s[tail]= s[tail], s[head]
            head+=1
            tail-=1
            # print(s)     time: O(n/2)
            
