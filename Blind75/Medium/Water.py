# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height) - 1
        left = 0
        right = len(height) - 1
        area = length * min(height[left], height[right])
        while (left != right):
            if height[left] > height[right]:
                right -= 1
            elif height[right] >= height[left]:
                left += 1
            x = (right - left) * min(height[left], height[right])
            if x > area:
                area = x
        return area 
