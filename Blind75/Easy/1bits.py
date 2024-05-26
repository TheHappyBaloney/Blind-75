# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        res = bin(n)
        for i in range(len(res)):
            if res[i] == '1':
                c += 1
        return c
