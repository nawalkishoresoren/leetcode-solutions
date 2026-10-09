class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        longest_seq = 0

        for num in seen:
            if num-1 not in seen:
                streak = 1
                while num+1 in seen:
                    streak += 1
                    num += 1
                longest_seq = max(longest_seq,streak)
        return longest_seq

        