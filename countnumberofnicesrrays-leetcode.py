class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        odd=0
        count=0
        start = 0
        for i in range(len(nums)):
            if nums[i]%2==1:
                odd+=1
            if odd>k:
                l+=1
                start=l
                odd-=1
            if odd==k:
                count+=1
                while nums[l]%2!=1:
                    count+=1
                    l+=1
            if odd==k and nums[i]%2==0:
                for j in range(start,l):
                    count+=1
        return count
