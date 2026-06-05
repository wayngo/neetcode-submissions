class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #to compare two strings to one another and see if they are equal in any order

        #create a hashmap for each string 

        #iterate through the lengths of the strings that we are given and add them to their 
        #own respective hashmap

        #as we are iterating through the lengths of each string we increment the key value for each character
        #every time we encounter it 

        #after adding the character counts for each string what we do is we just return true/false if the two maps 
        #are equal 

        if len(s) != len(t):
            return False 

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1
        return countS == countT