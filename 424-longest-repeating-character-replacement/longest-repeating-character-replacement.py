class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freqDict = defaultdict(int)
        maxLength = 0
        maxFreq = 0
        left, right = 0, 0
        while right < len(s):
            freqDict[s[right]] += 1
            maxFreq = max(maxFreq, freqDict[s[right]])

            if (right - left + 1) - maxFreq > k:
                freqDict[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, (right-left+1))
            right += 1

        return maxLength
            

        