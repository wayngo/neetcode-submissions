class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # two nested for loops 
        #check if our out forloop value is equal to our inner forloop value 
        

        #use set
        #for loop add elements to that set
        #check if the element is inside the array 
        #if it is return true 
        #if not add the elemnt and move on 
        #at the end if we dont return true, we return false 
        duplicate = set() 
        for num in nums:
            if num in duplicate:
                return True 
            duplicate.add(num)
        return False
