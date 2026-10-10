class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charFreq = [0]*256
        left, right, maxLength = 0, 0, 0
        while right<len(s):
            charFreq[ord(s[right])] += 1

            while charFreq[ord(s[right])] > 1:
                charFreq[ord(s[left])] -= 1
                left += 1
            
            maxLength = max(maxLength, right-left+1)
            right += 1
        return maxLength
        