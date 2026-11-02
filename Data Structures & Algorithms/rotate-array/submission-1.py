class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        # k = k % len(nums)

        # [1,2,3,4 | 5,6,7,8] 
        # 8 7 6 5  |  4 3 2 1]  O(n)
        # 5 6 7 8  |  1 2  3 4   O(k)  
        #                         O(n - k)  = O(2n) = O(n)

        # [5,6,7,8 | 1,2,3,4 ]
        k = k % len(nums)
        def reverse(l,r):
            while l < r:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0,len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)




        





