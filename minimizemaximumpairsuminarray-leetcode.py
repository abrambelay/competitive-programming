class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        minmax = 0
        n = len(nums)
        for i in range(n//2):
            minmax = max(minmax,nums[i]+nums[n-i-1])
        return minmax
