class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort() 
            print(temp)
            diff = temp[1]-temp[0]               
            for j in range(2,len(temp)):
                if temp[j]-temp[j-1]!=diff:
                    res.append(False)
                    break
            if len(res)<i+1:res.append(True)
        return res
