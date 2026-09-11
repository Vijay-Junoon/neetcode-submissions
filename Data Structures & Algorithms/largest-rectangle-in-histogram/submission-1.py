class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack  = []
        mArea = 0

        for i in range(len(heights)+1):
            height = 0 if i == len(heights) else heights[i]

            while stack and heights[stack[-1]] > height:
                ind = stack.pop()
                h = heights[ind]
                w = i if not stack else i - stack[-1] - 1
                mArea = max(mArea,h * w)

            stack.append(i)
        
        return mArea