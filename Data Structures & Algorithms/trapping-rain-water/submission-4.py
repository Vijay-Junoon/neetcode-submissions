class Solution:
    def trap(self, height: List[int]) -> int:
        
        lmax = [0] * len(height)
        rmax = [0] * len(height)

        lmax[0] = height[0]
        rmax[-1] = height[-1]

        for i in range(1,len(height)):
            lmax[i] = max(lmax[i-1],height[i])
        
        for i in range(len(height)-2,-1,-1):
            rmax[i] = max(rmax[i+1],height[i])
        
        water = 0

        for i in range(len(height)):
            w = min(lmax[i],rmax[i]) - height[i]
            if w > 0:
                water += w
        
        return water