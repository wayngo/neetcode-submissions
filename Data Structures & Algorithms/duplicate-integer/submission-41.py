class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ContainsDuplicate = set()

        for num in nums:
            if num in ContainsDuplicate:
                return True
            ContainsDuplicate.add(num)
        return False