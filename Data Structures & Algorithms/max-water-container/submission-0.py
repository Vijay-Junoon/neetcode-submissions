class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = 0
        while i < j:
            w = j - i
            h = min(heights[j],heights[i])
            maxArea = max(maxArea,w * h)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maxArea