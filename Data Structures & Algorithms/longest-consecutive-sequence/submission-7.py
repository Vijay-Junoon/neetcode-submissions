class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        mLen = 0
        for i in nums:
            cnt = 1
            while i + cnt in nums:
                cnt += 1
            mLen = max(mLen,cnt)
        return mLen 
