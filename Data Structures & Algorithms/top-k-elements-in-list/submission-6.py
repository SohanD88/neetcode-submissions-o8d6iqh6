class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        res = []
        for i in range(len(nums)):
            hm[nums[i]] = 1 + hm.get(nums[i], 0)

        for i in range(k):
            maxKey = max(hm, key = hm.get)
            res.append(maxKey)
            del(hm[maxKey])

        return res