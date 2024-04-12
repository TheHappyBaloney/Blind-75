# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len( nums )
        a = sum( nums )
        b = n * ( n + 1 ) // 2

        c = b - a

        return c 
