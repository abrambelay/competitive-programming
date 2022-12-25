class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        max=0
        hashset = set()
        while r<len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                r+=1
            else:
                hashset.discard(s[l])
                l+=1
            if max<r-l:max=r-l
        return max
