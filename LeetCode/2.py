# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_num(l):
            num = ''
            while True:
                num += str(l.val)
                if l.next == None:
                    break
                l = l.next
            return int(num[::-1])
        num1, num2 = get_num(l1),get_num(l2)
        ret_num = str(num1+num2)
        #print("num1:",num1,"num2:",num2,"ret:",ret_num)
        for idx,val in enumerate(list(ret_num)):
            val = int(val)
            if idx == 0:
                new_node = ListNode(val)
                prev_node = new_node
            else:
                new_node = ListNode(val)
                new_node.next = prev_node
                prev_node = new_node
        return new_node
