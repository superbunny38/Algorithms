# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(-1)
        front1, front2 = list1, list2
        cur = ListNode(-1)
        dummy = cur
        while True:
            if front1 != None and front2 != None:
                val1,val2 = front1.val,front2.val
                if val1<val2:
                    cur.next = front1
                    print(f">>{front1.val}",end = "")
                    front1 = front1.next
                    cur = cur.next
                    
                else:
                    cur.next = front2
                    print(f">>{front2.val}", end = "")
                    front2 = front2.next
                    cur = cur.next
            elif front1 == None and front2 != None:
                cur.next = front2
                print(f">>{front2.val}", end = "")
                front2 = front2.next
                cur = cur.next
            elif front2 == None and front1 != None:
                cur.next = front1
                print(f">>{front1.val}", end = "")
                front1  = front1.next
                cur = cur.next
            else:
                break
        
        return dummy.next
