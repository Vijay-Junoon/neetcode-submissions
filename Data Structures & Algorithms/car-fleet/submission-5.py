class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = []
        for i in range(len(position)):
            distance = target - position[i]
            time = distance/speed[i]
            arr.append((position[i],time))
        
        arr.sort(reverse = True)
        
        fleets = 0
        mTime = 0
        for p,t in arr:
            if t > mTime:
                mTime = t
                fleets += 1
        
        return fleets