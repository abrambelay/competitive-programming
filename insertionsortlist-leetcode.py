class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev , current = head , head.next
        while current:
            if current.val>=prev.val:
                current , prev = current.next, current
                continue
            temp = dummy
            while current.val > temp.next.val:
                temp = temp.next
            prev.next = current.next
            current.next = temp.next
            temp.next = current
            current = prev.next
        return dummy.next
