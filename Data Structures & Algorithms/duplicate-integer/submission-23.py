class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #iterate through the array 
        #check if a value has been seen twice
        #return true or false depending on if a value duplicates

        container = set()

        for num in nums:
            if num in container:
                return True
            container.add(num)
        return False