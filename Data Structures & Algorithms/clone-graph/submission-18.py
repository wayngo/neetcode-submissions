"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None

        # 1. Create MAP to store original nodes -> copied nodes

        # 2. Run dfs on our given node list

        # 3. Create copies of the nodes we are given 

        # 4. Go through neighboring nodes of our original list and add them to our copied nodes
        #    neighbors list

        # 5. 