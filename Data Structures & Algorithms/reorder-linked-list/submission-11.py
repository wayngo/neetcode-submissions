# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # we are given a linked list
        # reorder them in a way where it lists our smallest nodes, and our biggest nodes one after the other.

        # what if we divide our list in half
        # first half -> our smallest numbers increasing 
        # second half -> biggest numbers decreasing 

        # take the middle point of our list, and once we reach it
        # we can take the values in front of the middle and reverse it

        # reverseing a linked list -> merging two linked list together

        # 1. fast and slow pointers:
            # we have one pointer moving at the speed of 1, and
            # another moving at the speed of 2. 
                # why this works:
                    # by doing this by the time our fast pointer
                    # reaches the end of the list our slow pointer will
                    # be at the middle of the list.

        #2. for our values in front of our slow pointer we have 
        # reverse them (reverse a linked list)
        
        #

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        secondListCurrent = slow.next
        slow.next = None 
        previous = None

        while secondListCurrent:
            temp = secondListCurrent.next
            secondListCurrent.next = previous
            previous = secondListCurrent
            secondListCurrent = temp
        first, second = head, previous

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        







