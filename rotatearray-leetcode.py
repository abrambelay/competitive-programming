class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):k=k%len(nums)
        nums.reverse()
        nums[k:]=list(reversed(nums[k:]))
        nums[:k]=list(reversed(nums[:k]))
        
