class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j,k = i+1,len(nums)-1

            while j < k:
                t_sum = nums[j] + nums[k]

                if t_sum + nums[i] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j+=1
                    
                    k-=1
                    while k > i and nums[k] == nums[k+1]:
                        k-=1

                elif t_sum + nums[i] < 0:
                    j+=1
                else:
                    k-=1
        
        return res

