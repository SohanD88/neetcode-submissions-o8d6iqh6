class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        cur = []

        def dfs(i, summ):
            if summ == target:
                res.append(cur.copy())
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if summ + candidates[j] > target:
                    break
               
            
                cur.append(candidates[j])
                dfs(j + 1, summ + candidates[j])
                cur.pop()

        dfs(0, 0)
        return res

        