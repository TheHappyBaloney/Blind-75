# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        a.sort()
        b = list(t)
        b.sort()

        if len(a) != len(b):
            return False
    
        else:
            for i in range (len(a)):
                if a[i] != b[i]:
                    return False
            return True
            
