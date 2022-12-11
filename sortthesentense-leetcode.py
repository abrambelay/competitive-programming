class Solution(object):
    def sortSentence(self, s):
        news=''
        for i in range(1,10):
            start = 0
            for j in range(len(s)):
                if s[j]==str(i):
                    if str(i)=='1':
                        news=news+s[start:j]
                    else:
                        news=news+' '+s[start:j]
                if s[j]==' ':
                    start=j+1
        return news
