class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        order = []

        for i in range(len(position)):
            d = target - position[i]
            t = d/speed[i]
            order.append([position[i],t])

        order = sorted(order, key = lambda x : x[0],reverse = True)
        
        time = 0
        fleet = 0
        for d,t in order:
            if t > time:
                time = t
                fleet += 1
        return fleet