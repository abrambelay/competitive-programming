class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        student = 0
        tot = 0
        for i in range(len(chalk)):
            tot+=chalk[i]
        chalks=k%tot
        while True :
            if chalks >= chalk[student]:
                chalks-=chalk[student]
                student+=1
            else:
                return student
