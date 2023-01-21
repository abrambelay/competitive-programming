class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        hashmap = {}
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if stack:
                hashmap[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        for indx,num in enumerate(nums1):
            ans.append(hashmap.get(num,-1))
        return ans
