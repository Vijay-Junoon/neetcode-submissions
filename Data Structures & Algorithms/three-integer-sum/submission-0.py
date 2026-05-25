class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:
                mySum = nums[j] + nums[k] 
                if mySum == -nums[i]:
                    res.add((nums[i],nums[j],nums[k]))
                if mySum < -nums[i]:
                    j+=1
                else:
                    k-=1
        return [list(i) for i in res]
            