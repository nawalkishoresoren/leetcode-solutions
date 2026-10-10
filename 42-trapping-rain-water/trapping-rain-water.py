class Solution:
    def trap(self, height: list[int]) -> int:
        maxWater = 0
        left, right = 0, len(height)-1
        maxLeft, maxRight = height[left], height[right]

        while left<right:
            if maxLeft <= maxRight:
                maxWater += (maxLeft - height[left])
                left += 1
                maxLeft = max(maxLeft, height[left])
            else:
                maxWater += (maxRight - height[right])
                right -= 1
                maxRight = max(maxRight, height[right])
        
        return maxWater

        