class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        lst = []
        while current:
            lst.append(current.val)
            current = current.next
        l=0
        r=len(lst)-1
        maxS = 0
        while l<r:
            maxS = max(maxS,lst[r]+lst[l])
            l+=1
            r-=1
        return maxS
