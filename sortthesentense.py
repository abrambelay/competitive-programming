class Solution(object):
    def sortSentence(self, s):
        start=0
        news=''
        for i in range(1,10):
            for j in range(len(s)):
                if s[j]==str(i):
                    if str(i)=='1':
                        news=news+s[start:j]
                    else:
                        news=news+' '+s[start:j]
                if s[j]==' ':
                    start=j+1
            start = 0
        return news
