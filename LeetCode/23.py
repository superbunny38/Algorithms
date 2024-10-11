import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        ret = []
        for ll in lists:
            node = ll
            if node:
                while True:
                    heapq.heappush(hq,node.val)
                    if node.next != None:
                        node = node.next
                    else:
                        break
 
        if hq:
            while hq:
                popped = ListNode(heapq.heappop(hq))
                if len(ret) == 0:
                    head = popped
                    prev = head
                else:
                    prev.next = popped
                    prev = popped
                ret.append(prev)
            
            return head

        else:
            return 
