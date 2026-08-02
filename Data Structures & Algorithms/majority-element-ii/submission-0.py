class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hash = {}
        res = set()
        for n in nums:
            hash[n] = hash.get(n,0) + 1
            if hash[n] > len(nums)//3:
                res.add(n)
        
        return list(res)