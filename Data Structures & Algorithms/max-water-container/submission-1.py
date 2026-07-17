class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mArea = 0
        l,r = 0,len(heights)-1
        while l < r:
            h = min(heights[l],heights[r])
            w = r - l
            mArea = max(mArea,h*w)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return mArea