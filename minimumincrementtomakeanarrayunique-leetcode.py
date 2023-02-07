class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        minI = 0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                add = nums[i-1] - nums[i]+1
                minI += add
                nums[i] += add
        return minI
