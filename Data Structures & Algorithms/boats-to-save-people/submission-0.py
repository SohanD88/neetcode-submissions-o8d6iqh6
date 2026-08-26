class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if l == r:
                res += 1
                break
            elif people[l] + people[r] > limit and l < r:
                res += 1
                r -= 1

            elif people[l] + people[r] <= limit and l < r :
                l += 1
                r -= 1
                res += 1 

        return res

                