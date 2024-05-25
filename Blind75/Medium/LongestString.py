# 2745. Construct the Longest New String

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        c = z * 2

        n = min( x , y )
        c += n * 4
        x -= n
        y -= n

        if x > 0 or y > 0 :
            c += 2
        return c 
