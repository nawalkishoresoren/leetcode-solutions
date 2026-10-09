class Solution {
public:
    int longestConsecutive(vector<int>& nums) 
    {
        unordered_set<int>seen(nums.begin(),nums.end());
        int longest_seq = 0;

        for(auto num:seen)
        {
            if(seen.find(num-1)==seen.end())
            {
                int streak = 1;
                while(seen.find(num+1)!=seen.end())
                {
                    streak++;
                    num++;
                }
                longest_seq = max(longest_seq,streak);
            }
        }
        return longest_seq;
    }
};