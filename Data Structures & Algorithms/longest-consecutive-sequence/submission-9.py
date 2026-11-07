class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        mLen = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                cnt = 1
                while num + cnt in nums:
                    cnt += 1
                
                mLen = max(mLen,cnt)
        
        return mLen