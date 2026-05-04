# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #create a list, levels inside that list

        #create a list for the levels
        #Create a queue and add our root to it
        #check if our queue contains nodes inside of it (has something)
        #create a levels list and iterate through our queue (for loop)
        #assign a node varaible from the top of our queue (popleft)
        #if our node is there we add our current node to our level list 
        #add left node and right node to our q 
        #check if there anything inside our level listand then add that to our result list
        #return result

        res = [] 

        q = collections.deque() 
        q.append(root)

        while q:
            level = []
            qlength = len(q)
            for i in range(qlength):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


