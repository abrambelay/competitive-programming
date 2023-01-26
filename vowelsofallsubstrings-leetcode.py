class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        count = 0
        for i,char in enumerate(word):
            if char in "aeiou":
                count += (i+1)*(n-i)
        return count
