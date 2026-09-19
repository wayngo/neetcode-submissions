"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copiedValues = {None: None}
        cur = head

        while cur:
            copy = Node(cur.val)
            copiedValues[cur] = copy
            cur = cur.next
        
        cur = head

        while cur:
            copy = copiedValues[cur]
            copy.next = copiedValues[cur.next]
            copy.random = copiedValues[cur.random]
            cur = cur.next
        return copiedValues[head]