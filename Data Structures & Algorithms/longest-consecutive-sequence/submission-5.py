class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        
        
        resArr = []
        nums = list(set(nums))
        nums.sort()
        print(nums)
        cntArr = []
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                cnt += 1
            else:
                cntArr.append(cnt)
                cnt = 0
                continue
        print(cnt)
        return max(cntArr)+1 if cntArr and max(cntArr) > cnt else cnt+1
            
