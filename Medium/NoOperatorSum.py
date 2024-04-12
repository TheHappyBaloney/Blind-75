# 371. Sum of Two Integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        d = 0xffffffff
        
        while ( b & d != 0 ):
            c = ( a & b ) << 1
            a = a ^ b
            b = c
        
        return a & d if b > 0 else a
