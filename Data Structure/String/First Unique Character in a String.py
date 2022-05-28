# LeetCode: 387.First Unique Character in a String

'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.'''


# APPROACH1: implementing own hashmap with value:list of count, index
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for k in s:
            if k in hashmap:
                hashmap[k][0]+=1
            else:
                hashmap[k]=[1,s.index(k)]
        # print(hashmap)
        for i in hashmap.values():
            if i[0]==1:
                return i[1]
        return -1
    
#     time: O(n), Space: O(1) because English alphabet contains 26 letters.

# APPRAOCH2: using builtin counter 
# build hash map : character and how often it appears using built-in Counter
        count = collections.Counter(s)
        print(count)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1 
#     time: O(n), Space: O(1) because English alphabet contains 26 letters.
                
