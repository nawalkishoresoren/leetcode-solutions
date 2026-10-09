class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for index, num in enumerate(nums):
            newTarget = target - num

            if newTarget in seen:
                return [seen[newTarget], index]

            seen[num] = index
        return [-1,-1]
        