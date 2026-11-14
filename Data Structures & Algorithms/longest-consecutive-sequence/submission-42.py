class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        streak = 0 
        
        for num in values:
            length = 1 
            if (num - 1 ) not in values:
                while (num + length) in values:
                    length += 1
                streak = max(streak, length)
        return streak


