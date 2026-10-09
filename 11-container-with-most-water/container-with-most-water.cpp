class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0 , right = height.size()-1;
        int maxWater = 0, currWater = 0;
        while(left<right)
        {
            if(height[left]<=height[right])
            {
                currWater = height[left] * (right-left);
                left++;
            }
            else
            {
                currWater = height[right] * (right - left);
                right--;
            }
            maxWater = max(maxWater,currWater);
        }
        return maxWater;
        
    }
};