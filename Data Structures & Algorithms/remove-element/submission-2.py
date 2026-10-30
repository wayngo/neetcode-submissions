class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
          # 1 2 3 4 5 5 1 2      
        
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

          # expected: 1 2 3 4 1 2 5 5 