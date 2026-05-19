class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #find anagrams in our array full of strings and put anagrams into their own lists 

        #create a list to store our anagram values 
        
        #iterate through our array and for every string we can count the amount of times each character appears

        #based on how many times they appear what we can do is use that count as a key to direct where each anagram/string belongs to 

        #at the end we can return a list containing all of the sublists that we are given 

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ ord("a") - ord(c)] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())
