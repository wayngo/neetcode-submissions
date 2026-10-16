class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # given an array of nums and we want to reutrn a list of all unique combos!


        res = []


        def dfs(i, cur, total):
            #check if total = target
                # return
            #check if we are out of bounds or target greater than target
                # return
            #explore the other paths

            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res