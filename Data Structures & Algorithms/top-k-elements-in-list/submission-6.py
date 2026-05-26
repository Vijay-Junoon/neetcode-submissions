class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) < 2:
            return nums

        hash = dict()
        for i in nums:
            hash[i] = hash.get(i,0) + 1

        
        arr = []
        for key,val in hash.items():
            arr.append([key,val])

        arr = sorted(arr, key = lambda x : x[1],reverse = True)
        print(arr)
        res = [arr[i][0] for i in range(len(arr)) if i < k]
        return res