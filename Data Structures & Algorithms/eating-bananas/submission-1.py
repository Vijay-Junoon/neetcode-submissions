class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def computeHours(bananas):
            hours = 0
            for p in piles:
                hours += math.ceil(p/bananas)
            
            return hours


        l,r = 1, max(piles)
        ans = r

        while l <= r:
            bananas = (l+r)//2
            hours = computeHours(bananas)
            if hours <= h:
                ans = bananas
                r = bananas -  1
            else:
                l = bananas + 1
        
        return ans