class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2
            #left half is sorted!
            if target == nums[m]:
                return m
            if nums[m] >= nums[l]:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

                # 4 5 1 2 3 
            #right half is sorted
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

