class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        windowSum = 0
        totalSum = 0
        maxCard = 0
        l, r, = 0, n-k-1
        for i in range(n):
            totalSum += cardPoints[i]
            if i==(r):
                windowSum = totalSum
        maxCard = totalSum - windowSum
        while r<n-1:
            windowSum += cardPoints[r+1]
            windowSum -= cardPoints[l]
            maxCard = max(maxCard,totalSum - windowSum)
            l+=1
            r+=1
        return maxCard
