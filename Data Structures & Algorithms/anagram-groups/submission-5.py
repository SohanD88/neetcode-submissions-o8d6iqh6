class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        res = []
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            hm[key].append(strs[i])

        for i in hm.values():
            res.append(i)

        return res