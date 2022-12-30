class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        prev=0
        next=1
        for i in range(n-1):
            prev ,next = next ,next+prev
        return next
