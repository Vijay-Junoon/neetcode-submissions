class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxCnt,cnt = 0,0
        for i in nums:
            if i-1 not in nums:
                cnt = 1
                while i + cnt in nums:
                    cnt += 1
            maxCnt = max(maxCnt,cnt)
        return maxCnt
