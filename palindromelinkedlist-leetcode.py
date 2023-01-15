class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        prev = None
        current = head
        while current:
            lst.append(current.val)
            next = current.next
            current.next = prev
            prev = current
            current = next
        for i in lst:
            if i == prev.val:
                prev=prev.next
            else:
                return False
        return True
