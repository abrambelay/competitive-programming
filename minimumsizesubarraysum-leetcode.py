class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,tot = 0,0
        min_val = len(nums)+1
        for i in range(len(nums)):
            tot += nums[i]
            while tot>=target:
                min_val=min(min_val,i+1-l)
                tot -= nums[l]
                l+=1
        if min_val>len(nums):
            return 0
        else:
            return min_val
