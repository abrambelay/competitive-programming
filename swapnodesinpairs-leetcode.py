# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        node1 = None
        node2 = None 
        if dummy.next:
            node1 = dummy.next
            node2 = node1.next
        while node1 and node2:
            nextNode = node2.next
            prev.next = node2
            node2.next = node1
            node1.next = nextNode
            prev = node1
            if nextNode:
                node1 = nextNode
                node2 = nextNode.next
            else:
                break
        return dummy.next
