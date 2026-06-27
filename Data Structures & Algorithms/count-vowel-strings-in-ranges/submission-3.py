class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        hmVow = {"a", "e", "i", "o", "u"}

        prefSum = [0] * (len(words) + 1)
        prevVal = 0 
        res = []

        for i in range(len(words)):
            if words[i][0] in hmVow and words[i][-1] in hmVow:
                prevVal +=1

            prefSum[i+1] = prevVal

        
        for query in queries:
            l, r = query
            res.append(prefSum[r+1] - prefSum[l])

        return res

