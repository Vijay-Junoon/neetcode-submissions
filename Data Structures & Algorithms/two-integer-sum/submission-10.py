class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}
        for a in range(len(nums)):
            b = target - nums[a]
            if b in hash:
                return [hash[b],a]
            hash[nums[a]] = a