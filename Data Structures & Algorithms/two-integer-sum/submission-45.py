class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for index, number in enumerate(nums):
            diff = target - number

            if diff in difference:
                return [difference[diff], index]
            
            difference[number] = index
        return []