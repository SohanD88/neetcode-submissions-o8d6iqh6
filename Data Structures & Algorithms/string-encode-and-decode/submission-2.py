class Solution:

    def encode(self, strs: List[str]) -> str:
        encStr = ""
        delimiter = "."
        for i in range(len(strs)):
            encStr = encStr + strs[i] + delimiter

        return encStr


    def decode(self, s: str) -> List[str]:
        res = []
        currStr = ""
        for i in range(len(s)):
            if s[i] != ".":
                currStr += s[i]
            else:
                res.append(currStr)
                currStr = ""

        return res