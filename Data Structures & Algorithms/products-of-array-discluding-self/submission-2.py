class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        postFix = 1

        for i in range(1,len(nums)):
            res[i] = nums[i-1] * res[i-1]

        for i in range(len(nums)-2,-1,-1):
            postFix = nums[i+1] * postFix
            res[i] = res[i] * postFix

        return res           