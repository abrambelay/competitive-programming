class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head
        temp = self.divide(head)
        right = temp.next
        temp.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeSort(left,right)
    def divide(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def mergeSort(self,l1,l2):
        dummy = current =  ListNode()
        while l1 and l2:
            if l1.val>l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next
