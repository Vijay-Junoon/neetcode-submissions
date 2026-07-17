class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lMax = [0] * n
        rMax = [0] * n

        for i in range(n):
            lMax[i] = max(lMax[i-1],height[i])
        
        rMax[-1] = height[-1]
        for i in range(n-2,-1,-1):
            rMax[i] = max(rMax[i+1],height[i])
        print(lMax,rMax)
        mArea = 0
        for i in range(n):
            water = min(rMax[i],lMax[i]) - height[i]
            if water > 0:
                mArea += water
        return mArea