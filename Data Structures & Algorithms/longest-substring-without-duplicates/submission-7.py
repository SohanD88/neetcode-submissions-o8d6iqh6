class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l, r = 0, 1
        currStr = set()
        maxLen = 0
        while r < len(s):
            currStr.add(s[l])
            while r < len(s) and s[r] not in currStr:
                currStr.add(s[r])
                r += 1

            else:
                maxLen = max(maxLen, len(currStr))
                currStr = set()
                l += 1
                r = l+1
        return maxLen

