class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        #using deafaultdict accounts for keys that dont exist, int is equal to 0 so it 
        #intializes any new added values to 0 
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
            res = max(res, mp[num])
        return res
    #updates the bondaries not every element within the bondaries 
    # for example if we have 1 , 2 , 3  and 5 , 6 
    # if we add 4 we set num[4] = to 3 + 1 + 2 
    # we also update the boundaries so mp[4 - 3] = mp[1] = mp[4] 


