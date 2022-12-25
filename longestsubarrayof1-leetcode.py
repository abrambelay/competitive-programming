class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros=0
        l=0
        max=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            if zeros>1:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if max<i-l:max=i-l
        return max
