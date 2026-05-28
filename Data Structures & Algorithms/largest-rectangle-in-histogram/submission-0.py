class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mArea = 0
        stack = []
        n = len(heights)
        for i in range(n+1):
            curr = 0 if i == n else heights[i]
            while stack != [] and curr < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if stack == [] else i - stack[-1] - 1
                mArea = max(mArea,height * width)
            stack.append(i)
            
        return mArea