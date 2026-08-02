class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq= {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        freq_arr = [(v,k) for k,v in freq.items()]
        freq_arr.sort(reverse = True)
        res = [y for x,y in freq_arr[:k]]
        return res