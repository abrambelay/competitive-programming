class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins = 0
        for i in range(len(piles)//3):
            coins+=piles[len(piles)-(2*i)-2]
        return coins
