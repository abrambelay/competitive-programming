class Solution(object):
    def rearrangeArray(self , nums):
        nums.sort()
        array=[]
        i=0
        j=len(nums)-1
        while len(array)!=len(nums):
            array.append(nums[i])
            i+=1
            if j>i:
                array.append(nums[j])
                j-=1
        return array
