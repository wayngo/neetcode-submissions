class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        biggest = nums[0]
        res = {}

        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1
            if res[nums[i]] > (len(nums)/2) : 
                biggest = nums[i]
        return biggest

