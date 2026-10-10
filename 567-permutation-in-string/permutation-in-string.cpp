class Solution {
public:
    bool checkInclusion(string s1, string s2) 
    {
        vector<int>s1Freq(26,0);
        vector<int>s2Freq(26,0);

        for(auto c:s1)
        {
            s1Freq[c-'a']++;
        }

        int left = 0, right = 0;

        while(right < s2.length())
        {
            s2Freq[s2[right] - 'a']++;
            if((right-left+1) > s1.size())
            {
                s2Freq[s2[left]-'a']--;
                left++;
            }
            if(s1Freq == s2Freq)
            {
                return true;
            }
            right++;
        }
        return false;
    }
};