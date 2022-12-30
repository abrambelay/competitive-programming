class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        res = 0
        for i in counter:
            if k-i in counter:
                if k-i==i:
                    res+=counter[k-i]//2
                else:
                    res += min(counter[k-i],counter[i])
                counter[k-i]=0
        return res
