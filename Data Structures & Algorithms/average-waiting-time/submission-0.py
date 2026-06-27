class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        total = 0

        for arrival, time in customers:
            if t > arrival:
                total += t - arrival
            else:
                t = arrival
            total += time
            t += time

        return total/len(customers)


