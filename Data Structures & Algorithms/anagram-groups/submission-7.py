from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        res = []
        for i in range(len(strs)):
            sort = tuple(sorted(strs[i]))
            hm[sort].append(strs[i])

        for i in hm.values():
            res.append(i)
        return res

