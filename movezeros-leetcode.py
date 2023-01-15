class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        n = len(nums)
        r = n
        for i in range(n):
            if nums[i]!=0:
                nums[l]=nums[i]
                l+=1
            else:
                r-=1
        for j in range(r,n):
            nums[j]=0
