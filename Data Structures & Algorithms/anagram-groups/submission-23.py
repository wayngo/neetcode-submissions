class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #no numbers, no special characters, and no uppercase letters

        #abc
        #[1,1,1,00000]
        #bca 
        #[1,1,1,0,0,0,... to 26] len of 26
        #[abc,bca]
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                #[0,0,0]
                count[ord("a") - ord(c)] += 1

            result[tuple(count)].append(s)
        return list(result.values())
            
        

        #