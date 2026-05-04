class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #two nested forloops that iterate and we can check if their values added up is equal to our target value 
        #N(n^2) too long 

        #HASHMAP
        #for loop 

        difference = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in difference:
                return [difference[diff], i]
            difference[n] = i 