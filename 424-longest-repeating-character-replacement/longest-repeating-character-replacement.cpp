class Solution {
public:
    int characterReplacement(string s, int k) 
    {
        int charFreq[26] = {0};
        int maxFreq = 0, maxLength = 0;
        int left= 0, right = 0;

        while(right<s.size())
        {
            charFreq[s[right] - 'A']++;
            maxFreq = max(maxFreq, charFreq[s[right]-'A']);

            if ((right - left + 1) - maxFreq > k)
            {
                charFreq[s[left] - 'A']--;
                left++;
            }
            maxLength = max(maxLength, (right - left + 1));
            right++;
        }
        return maxLength;
    }
};