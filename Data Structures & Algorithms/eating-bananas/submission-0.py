class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        min_speed = m

        def isValid(speed):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/speed)

            return total_time <= h

        low = 1
        high = m

        while low <= high:
            mid = (low + high)//2

            if isValid(mid):
                min_speed = mid
                high = mid-1
            else:
                low = mid+1

        return min_speed