class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            arr.append(sum)
        if arr[len(arr)-1]-arr[0]==0:
            return 0
        for i in range(1,len(arr)):
            if arr[i-1]==arr[len(arr)-1]-arr[i]:
                return i
        return -1
