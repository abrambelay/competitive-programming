#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            indx = i
            cur = arr[indx]
            for j in range(i+1,n):
                if arr[j]<cur:
                    cur = arr[j]
                    indx = j
            arr[i],arr[indx] = arr[indx],arr[i]
