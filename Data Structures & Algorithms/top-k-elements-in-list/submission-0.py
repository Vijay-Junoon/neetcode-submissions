class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        nums =  Counter(nums).most_common(k)
        res = []
        for i in nums:
            res.append(i[0])
        return(res)