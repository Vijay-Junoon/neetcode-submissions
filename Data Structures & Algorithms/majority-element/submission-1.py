class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hash = dict()

        for n in nums:
            hash[n] = hash.get(n,0) + 1
            if hash[n] > len(nums)//2:
                return n
        
        