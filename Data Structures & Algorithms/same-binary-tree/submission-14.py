# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]

        while stack:
            list1,list2 = stack.pop()

            if not list1 and not list2:
                continue
            if not list1 or not list2 or list1.val != list2.val:
                return False
            
            stack.append((list1.left, list2.left))
            stack.append((list1.right, list2.right))
        return True