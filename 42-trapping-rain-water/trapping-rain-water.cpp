class Solution {
public:
    int trap(vector<int>& height) 
    {
        int maxWater = 0;
        int left = 0, right = height.size()-1;
        int maxLeft = height[left], maxRight = height[right];

        while(left<right)
        {
            if(maxLeft <= maxRight)
            {
                maxWater += (maxLeft - height[left]);
                left++;
                maxLeft = max(maxLeft, height[left]);
            }
            else
            {
                maxWater += (maxRight - height[right]);
                right--;
                maxRight = max(maxRight, height[right]);
            }
        }
        return maxWater;
    }
};