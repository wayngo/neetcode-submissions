class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        CountS, CountT = {}, {}

        for i in range(len(s)):
            CountS[s[i]] = CountS.get(s[i], 0) + 1
            CountT[t[i]] = CountT.get(t[i], 0) + 1

        return CountS == CountT