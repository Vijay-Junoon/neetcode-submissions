class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,c,r = 0,0,len(nums)-1
        while c <= r:
            if nums[c] == 0:
                nums[l],nums[c] = nums[c],nums[l]
                l+=1
                c+=1
            elif nums[c] == 2:
                nums[c],nums[r] = nums[r],nums[c]
                r-=1
            else:
                c+=1