class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create a left pointer and right pointer
        # while loop with pointers l < r 
        # check if current pointer is a numnber (skip it)
        #compare the two pointers of a undercase letter 
        #return true/false

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isValid(s[l]):
                l += 1
            while l < r and not self.isValid(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def isValid(self, c):
        return ((ord('a') <= ord(c) <= ord('z') or 
                 ord('A') <= ord(c) <= ord('Z')) or
                 ord('0') <= ord(c) <= ord('9'))