class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for IndexKey, numValue in enumerate(nums):
            TargetDiff = target - numValue

            if TargetDiff in difference:
                return [ difference[TargetDiff], IndexKey]
            difference[numValue] = IndexKey
        
        return []
        