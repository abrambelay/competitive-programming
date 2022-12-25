class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        windowsum=0
        subarray=0
        l=0
        for i in range(k):
            windowsum+=arr[i]
        if windowsum/k>=threshold:
            subarray+=1
        for i in range(k,len(arr)):
            windowsum+=arr[i]
            windowsum-=arr[l]
            if windowsum/k>=threshold:
                subarray+=1
            l+=1
        return subarray
