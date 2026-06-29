class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if (stone1 == stone2):
                continue

            elif -stone1 > -stone2:
                stone1 = stone1 - stone2
                heapq.heappush(stones, stone1)

            else:
                stone2 = stone2 - stone1
                heapq.heappush(stones, stone2)


        if not stones:
            return 0
        else:
            return -(heapq.heappop(stones))
        