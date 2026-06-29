class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Get max of piles and set that to be your eating speed
        l, r = 1, max(piles)
        minSpeed = r
        while l <= r:
            mid = (l + r) // 2
            time = 0 
            for val in piles:
                time += math.ceil(float(val) / mid)

            if time <= h:
                minSpeed = mid
                r = mid - 1

            else:
                l = mid + 1

        return minSpeed