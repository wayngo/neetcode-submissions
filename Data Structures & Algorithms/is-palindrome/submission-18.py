class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if not c.isalnum():
                continue
            newStr += c.lower()
        return newStr == newStr[::-1]
