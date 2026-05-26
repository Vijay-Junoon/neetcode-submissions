class Solution:
    def trap(self, height: List[int]) -> int:
        lMax,rMax = [0] * len(height),[0] * len(height)
        m = 0
        for i in range(len(height)):
            m = max(m,height[i])
            lMax[i] = m
        

        m = 0
        for i in range(len(height)-1,-1,-1):
            m = max(m,height[i])
            rMax[i] = m
        
        water = 0
        for i in range(len(height)):
            t = min(lMax[i],rMax[i]) - height[i]
            if t > 0:
                water += t
        return water