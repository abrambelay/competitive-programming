class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        start = 0
        end = 0
        max=0
        while end<len(nums):
            if nums[end]==0:
                zeros+=1
            if zeros>k:
                if nums[start]==0:
                    zeros-=1
                start+=1
            end+=1
            if max<=end-start:
                max=end-start
        return max
