class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 
        r = len(nums)-1
        while r>l:
            if nums[r]==0:
                r-=1
            else:
                if nums[l]==0 :
                    for i in range(l,r):
                        nums[i]=nums[i+1]
                    nums[r]=0
                    r-=1
                else:
                    l+=1
