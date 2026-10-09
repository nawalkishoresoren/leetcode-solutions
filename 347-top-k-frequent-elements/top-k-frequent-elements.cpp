class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        unordered_map<int,int>fmap;
        for(auto& num: nums)
        {
            fmap[num]++;
        }

        //Min heap
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;

        for(const auto& fp:fmap)
        {
            pq.push({fp.second,fp.first});
            if(pq.size()>k)
                pq.pop();
        }

        //Result
        vector<int>result;
        while(!pq.empty())
        {
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;
    }
};