# LeetCode: 383.Ransom Note

'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.'''

# APPROACH: create hashmap for ransomNote and magazine, then check if hashmap of ransomNote is in hashmap of magazine
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap_magazine={}
        hashmap_ransomNote={}
        
        for i in magazine:
            if i in hashmap_magazine:
                hashmap_magazine[i]+=1
            else:
                hashmap_magazine[i]=1
            
        for i in ransomNote:
            if i in hashmap_ransomNote:
                hashmap_ransomNote[i]+=1
            else:
                hashmap_ransomNote[i]=1
            
            # print(hashmap_ransomNote )
            # print(hashmap_magazine)
            
        for k in hashmap_ransomNote:
            if k in hashmap_magazine:
                if hashmap_ransomNote[k]>hashmap_magazine[k]:
                    return False
            else:
                return False
        return True    
#       time:O(length of ransomNote + length of magazine), space:O(1) bcoz of 26 alphabets


# APPROACH2: sort both strings and convert to lists, check if char of magazine exist in 0th index of ransomNote, if its there pop it. 
#           check in end if ransomeNote list is empty or not

        ran=list(sorted(ransomNote))
        mag=list(sorted(magazine))
        
        for char in mag:
            if ran and char==ran[0]:
                ran.pop(0)
        if ran:
            return False
        else:
            return True
#         time:O(nlogn) in best case, space:O(ransomNote.length+ magazine.length)


# APPROACH3: one-liner
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
# Time: O(m+n) with m and n being the lengths of the strings.


