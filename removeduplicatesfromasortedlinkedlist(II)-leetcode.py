class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        hashmap = {}
        while current:
            hashmap[current.val] = hashmap.get(current.val,0)+1
            current = current.next
        dummy = prev = ListNode()
        dummy.next = head
        current = prev.next
        while current:
            print(hashmap[current.val])
            if hashmap[current.val]<2:
                prev.next = current
                prev = prev.next
            current = current.next
        prev.next = None
        return  dummy.next
