class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowles = {'a','e','i','o','u'}
        num = 0
        l=0
        arr=[]
        for i in range(k):
            if s[i] in vowles:
                num+=1
        arr.append(num)           
        for i in range(k,len(s)):
            if s[l] in vowles:
                num-=1
            if s[i] in vowles:
                num+=1
            arr.append(num)
            l+=1
        return max(arr)
