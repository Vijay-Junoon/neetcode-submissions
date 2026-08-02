class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        nums = set(nums)
        mLength = 0
        for n in nums:
            if n-1 in nums:
                continue
            cnt = 1
            while n + cnt in nums:
                cnt += 1

            mLength = max(mLength,cnt)
        
        return mLength


