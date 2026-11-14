class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0 

        l = 0
        r = len(height) - 1 

        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax > rightMax:
                r -= 1
                rightMax = max(rightMax, height[r])
                
                area += rightMax - height[r]
            
            else:
                l += 1
                leftMax = max(leftMax, height[l])
                
                area += leftMax - height[l]
        return area
                
            