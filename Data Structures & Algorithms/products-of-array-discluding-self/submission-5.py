class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        #initialize array to len of array

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        #The goal for this problem is to multiply every number by the entire array
        #except for itself, what we can is use post and pre fixes were values are multiplied by 
        #the product of all elements towards its right and all products towards its left,
        #what this does is it creates a product of all integers on the left side of the array and
        #rightside where it avoids using the product of iteself.