# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sol = nums1 + nums2
        sol.sort()
        
        a = len(sol)
        if a % 2 != 0:
            avg = sol[ a // 2 ]
        else:
            hi = a // 2 - 1 
            lo = a // 2
            avg = ( ( sol[hi] + sol[lo] ) / 2 )
        
        return avg
