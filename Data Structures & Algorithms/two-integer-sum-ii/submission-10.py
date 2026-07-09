class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1 

        while l < r:
            cumulativeSum = numbers[l] + numbers[r]

            if cumulativeSum < target:
                l += 1
            elif cumulativeSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []
        