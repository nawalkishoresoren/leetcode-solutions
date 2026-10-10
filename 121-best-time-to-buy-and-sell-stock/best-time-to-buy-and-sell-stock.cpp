class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minSoFar = INT_MAX;
        int maxProfit = 0, currProfit = 0;
        for(auto price: prices)
        {
            minSoFar = min(minSoFar, price);
            currProfit = price - minSoFar;
            maxProfit = max(maxProfit, currProfit);
        }
        return maxProfit;
        
    }
};