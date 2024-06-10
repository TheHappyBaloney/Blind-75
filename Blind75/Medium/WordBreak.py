# 139. Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * n

        def solve( i , s ):
            if i < 0 :
                return True
            if dp[i] != -1:
                return dp[i] == 1
            for j in wordDict:
                sz = len(j)
                if i - sz + 1 >= 0 and s[i-sz+1:i+1] == j :
                     if solve(i - sz, s):
                        dp[i] = 1
                        return True
            dp[i] = 0
            return False

        return solve(n-1, s)
