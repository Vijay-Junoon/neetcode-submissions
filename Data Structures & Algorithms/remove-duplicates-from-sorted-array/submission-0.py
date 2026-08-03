class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        l,r = 0,0
        while r < len(nums):
            while r < len(nums) and nums[r] == nums[l]:
                r+=1
            if r < len(nums):
                nums[l+1],nums[r] = nums[r],nums[l+1]
                l+=1
                nums[r] = nums[l]
        
        return l+1
