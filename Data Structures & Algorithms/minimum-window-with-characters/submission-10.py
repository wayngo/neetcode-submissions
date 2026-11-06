class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        res = [-1,-1]
        resLength = float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1  
            if c in countT and countT[c] == window[c]:
                have += 1
           
            while have == need:
                if (r-l+1) < resLength:
                    res = [l,r]
                    resLength = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLength != float("infinity") else "" 