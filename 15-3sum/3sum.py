class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()

        for index, num in enumerate(nums):
            if(index>0 and nums[index-1] == num):
                continue
            
            target = -num
            left,right = index+1, len(nums)-1

            while(left<right):
                sum = nums[left] + nums[right]

                if(sum == target):
                    ans.append([num,nums[left],nums[right]])

                    while(left<right and nums[left] == nums[left+1]):
                        left += 1
                    
                    while(left<right and nums[right] == nums[right-1]):
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif(sum > target):
                    right -= 1
                else:
                    left += 1
        
        return ans
        