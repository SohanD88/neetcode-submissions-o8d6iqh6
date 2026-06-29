class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distArr = []


        for x, y in points:
            dist = math.sqrt((x**2) + (y**2))
            distArr.append([dist, [x, y]])

        heapq.heapify(distArr)
        res = []
        for i in range(k):
            dist, coordinates = heapq.heappop(distArr)
            res.append(coordinates)


        return res


