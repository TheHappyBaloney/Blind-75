# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        Max = 1
        Str = s[0]

        for i in range( len(s) - 1 ):
            for j in range( i + 1 , len(s) ):
                if j - i + 1 > Max and s[ i : j + 1 ] == s[ i : j + 1 ][ : : -1 ]:
                    Max = j - i + 1
                    Str = s[ i :  j + 1 ]

        return Str

