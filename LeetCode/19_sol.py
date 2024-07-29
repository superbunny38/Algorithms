# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        front,back = dummy,dummy
        
        for _ in range(n):
            front = front.next
        
        while front.next != None:
            front, back = front.next,back.next
        
        print("front val:",front.val)
        print("back val:",back.val)

        back.next = back.next.next
        
        return dummy.next
