class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cnt = 1
        while cnt in nums:
            cnt += 1
        
        return cnt