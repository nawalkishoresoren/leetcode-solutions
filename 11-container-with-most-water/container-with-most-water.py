class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height)-1
        maxWater, currWater = 0, 0
        while(left<right):
            if height[left]<=height[right]:
                currWater = height[left]*(right-left)
                left += 1
            else:
                currWater = height[right]*(right-left)
                right -= 1
            maxWater = max(maxWater,currWater)
        return maxWater

        