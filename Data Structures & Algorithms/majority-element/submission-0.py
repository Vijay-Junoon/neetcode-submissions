class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        q = len(nums)//2
        for n in nums:
            hash[n] = hash.get(n,0) + 1
            if hash[n] > q:
                return n