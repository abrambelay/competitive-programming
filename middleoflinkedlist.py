# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        size = 0
        current = head
        middle=head
        while True:
            if current.next==None:
                break
            else:
                current = current.next
                size+=1
        if size%2==0:
            for i in range(size//2):
                middle = middle.next
        else:
            for i in range(size//2+1):
                middle = middle.next
        return middle
