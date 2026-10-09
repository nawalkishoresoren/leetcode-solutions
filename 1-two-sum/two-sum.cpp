class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        unordered_map<int,int>umap; // num to index mapping
        
        for(int i=0;i<nums.size();i++)
        {
            int newTarget = target - nums[i];
            
            if(umap.find(newTarget)!=umap.end())
            {
                return {umap[newTarget],i};
            }
            umap[nums[i]] = i;
        }
        return {}; 
    }
};