"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #map of old nodes connected to copies

        #run dfs on original list
            #check if node exists within our map
            #create copies of specific nodes within our given list
            #map our old nodes to our newly copied nodes

            # go through our original lists neighbooring nodes and 
            # append them to our copied neighboring nodes
            # have our dfs function return the copy node
        
        # return our dfs function being called on our Node under the condition
        # that its null

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


