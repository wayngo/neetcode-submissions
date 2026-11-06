class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l, r = 0, len(nums)-1

        while l <= r:

            m = (r + l) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                #left side is sorted
                if nums[l] <= target < nums[m]:
                    r = m -1
                #if nums[r] < target or nums[m] > target:
                else:
                    l = m + 1
        
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r -= 1
                #right side is sorted
        return -1 

