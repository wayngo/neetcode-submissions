class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #search our array to see if theres a duplicate 


            #Iterate through our array 
                #simple for loop for nums
            #A way to store elements in our array to later on check if they appeared beforehand 
                #lets use a Set to store elements
                #.adds
            #if it appears more than once we turn a boolean value of true 
                # .contains
                #return True
            #if our iteration ends without finding a single duplicate we return false 
                #return False 
        
        duplicateValues = set() 

        for num in nums:
            if num in duplicateValues:
                return True
            duplicateValues.add(num)
        return False

        
