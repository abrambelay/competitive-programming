class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq, l, r, increment = 1, 0, 1, 0
        while r < len(nums):
            if increment > k:
                increment -= nums[r-1]-nums[l]
                l+=1
            if increment <= k:
                increment += (r-l)*(nums[r]-nums[r-1])
                if increment <= k:
                    maxFreq = max(maxFreq , r-l+1)
                r+=1
        return maxFreq
