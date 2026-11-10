class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        


        l, r = 1, max(piles)

        totalTime = r

        while l <= r:

            mid = ((r - l)//2) + l
            time = 0

            for i in range(len(piles)):
                time += math.ceil(float(piles[i] )/ mid)
            
            if time <= h:
                r = mid - 1
                totalTime = mid
            else:
                l = mid + 1
        return totalTime
            



