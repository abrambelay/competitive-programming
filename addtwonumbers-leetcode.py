# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        dummy = ListNode(0)
        node = dummy
        carry = 0
        while n1 or n2 or carry:
            c1 = n1.val if n1 else 0
            c2 = n2.val if n2 else 0
            carry , res = divmod(c1+c2+carry,10)
            node.next = ListNode(res) 
            node = node.next
            if n1:n1 = n1.next
            if n2:n2 = n2.next
        return dummy.next
