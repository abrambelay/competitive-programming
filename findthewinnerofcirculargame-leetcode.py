#recursive solution
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = []
        for i in range(1,n+1):
            lst.append(i)
        start = 0 
        def FindWinner(ind):
            if len(lst)==1:
                return lst[0]
            else:
                lst.pop(ind)
                start = ind%len(lst)
                return FindWinner((start + k-1)%len(lst))
        return FindWinner((k-1)%len(lst))
#itrative solution
"""
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = []
        for i in range(1,n+1):
            lst.append(i)
        start = 0
        while len(lst)>1:
            ind = (start + k-1)%len(lst)
            lst.pop(ind)
            start = ind%len(lst)
        return lst[0]
"""
