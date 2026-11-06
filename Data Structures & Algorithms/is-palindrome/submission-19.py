class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = []

        for c in s:
            if not c.isalnum():
                continue
            newStr.append(c.lower())
        newString = "".join(newStr)
        return newString == newString[::-1]
