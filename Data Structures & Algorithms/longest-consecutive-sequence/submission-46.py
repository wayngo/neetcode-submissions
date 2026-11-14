class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)

        longest = 0

        for num in values:
            if (num - 1 ) not in values:
                streak = 1

                while (num + streak) in values:
                    streak += 1
                longest = max(longest, streak)
        return longest

