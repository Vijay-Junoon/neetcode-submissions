class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        


        def returnHours(b):
            hours = 0
            for p in piles:
                hours += math.ceil(p/b)
            return hours






        l,r = 1, max(piles)
        ans = r
        while l < r:
            b = (l+r)//2
            hours = returnHours(b)
            if hours <= h:
                ans = b
                r = b
            else:
                l = b + 1
        return ans








