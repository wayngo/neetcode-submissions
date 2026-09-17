# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondList = slow.next
        slow.next = None
        prev = None

        while secondList:
            temp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = temp
        
        firstList, secondList = head, prev

        while secondList:
            #first node pooint it to a 2nd node 
            temp1, temp2 = firstList.next, secondList.next
            firstList.next = secondList
            secondList.next = temp1
            firstList = temp1 
            secondList = temp2
        
  



