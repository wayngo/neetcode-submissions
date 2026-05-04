class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contain = set()
        for num in nums:
            if num in contain:
                return True
            contain.add(num)
        return False
