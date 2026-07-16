class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash = dict()
        for i in nums:
            hash[i] = hash.get(i,0) + 1
        
        nums = set(nums)
        arr = []
        for key,val in hash.items():
            arr.append([val,key])
        
        arr.sort(reverse = True)
        ans = [arr[i][1] for i in range(k)]
        
        return ans
        
