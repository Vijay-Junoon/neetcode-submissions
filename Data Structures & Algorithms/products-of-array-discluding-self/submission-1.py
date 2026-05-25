class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        op = []

        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            pdt = math.prod(temp)
            op.append(pdt)
            temp.clear()
        return op
           