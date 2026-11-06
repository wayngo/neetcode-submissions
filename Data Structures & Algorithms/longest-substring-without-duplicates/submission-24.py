class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left pointer
        l = 0
        #map to store characters and their previous indexes
        mp = {}
        # count for longest string
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res
    
