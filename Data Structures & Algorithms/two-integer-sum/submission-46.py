class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceMap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in differenceMap:
                return [differenceMap[diff], i]
            
            differenceMap[n] = i
        return []

