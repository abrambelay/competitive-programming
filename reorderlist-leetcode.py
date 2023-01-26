class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        prev = None
        current = right
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt 
        left = head
        right = prev
        while right:
            nextLeft = left.next
            nextRight = right.next
            left.next = right
            right.next = nextLeft
            right = nextRight
            left = nextLeft
