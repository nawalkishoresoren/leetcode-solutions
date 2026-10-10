class Solution {
public:
    int lengthOfLongestSubstring(string s) 
    {
        int charFreq[256] = {0};
        int left = 0, right = 0, maxLength = 0;

        while(right<s.length())
        {
            charFreq[s[right]]++;
            while(charFreq[s[right]]>1)
            {
                charFreq[s[left]]--;
                left++;
            }
            maxLength = max(maxLength, right-left+1);
            right++;
        }
        return maxLength;
    }
};