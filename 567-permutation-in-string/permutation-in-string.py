class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = [0]*26
        s2Freq = [0]*26

        for c in s1:
            s1Freq[ord(c)-ord('a')] += 1
        
        left, right = 0, 0
        while right < len(s2):
            s2Freq[ord(s2[right]) - ord('a')] += 1

            if (right-left+1) > len(s1):
                s2Freq[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if s1Freq == s2Freq:
                return True
            
            right += 1
            
        return False