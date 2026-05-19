class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #a hashmap to store prior values that when added up to our current value equals to our target value

        #iterate through our array, and we check by finding the difference between our 
        #target value and our current value that we are on in the array 

        #for each iteration check if that value was already stored and if it is we return the index of 
        #the value we stored along with our current value in the iteration

        #at the end we just return an empty array to show we didnt find a two sum 


        difference = {} 

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in difference:
                return [difference[diff], i]
            difference[n] = i
