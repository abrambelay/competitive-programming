class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram = {}
        window = {}
        positions = []
        if len(p)<=len(s):
            for i in range(len(p)):
                anagram[p[i]]=1+anagram.get(p[i],0)
                window[s[i]]=1+window.get(s[i],0)
            if anagram==window:
                positions.append(0)
            l = 0
            for i in range(len(p),len(s)):
                window[s[l]]-=1
                if window[s[l]]==0:
                    window.pop(s[l])
                window[s[i]]=1+window.get(s[i],0)
                l+=1
                if anagram==window:
                    positions.append(l)
            return positions
