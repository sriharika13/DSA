# LeetCode: 557.Reverse Words in a String III

'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(" ")  #O(n)
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)
      
#  Time : O(n), Space: O(n)


