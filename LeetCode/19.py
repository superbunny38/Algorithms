# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 1
        cur_node = head
        ret = []
        left = None
        if head.next == None and n == 1:#경우 3
            return
        safe_int = 1
        while cur_node.next != None:
            print("\nval:",cur_node.val)
            print("size:",size)
            if size == n+safe_int:
                left = head
                print("left:",left.val)
            elif size>n+safe_int and left.next != None:
                left = left.next
                print("left:",left.val)

            cur_node = cur_node.next
            size +=1
        
        if size == 2:
            if n == 1:
                head.next = None
                return head
            elif n == 2:
                return head.next
            else:
                print(f"size: {size} n: {n}")


        last_node = cur_node
        # left = left.next
        print("\nend:",cur_node.val)
        if left != None:
            left = left.next
            print("final left:",left.val)
        if size-1 == n:
            left = head
        elif size == n:
            return head.next

        print("\nsize:",size)

        delete_node = left.next
        
        #left right 둘 다 있는 경우
        if delete_node.next != None:
            right = delete_node.next
            left.next = right
            del delete_node
            return head
        else:#right X
            left.next = None
            del delete_node
            return head            
