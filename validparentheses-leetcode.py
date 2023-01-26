class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        parentheses={
            '(':')',
            '[':']',
            '{':'}'
            }
        if len(s)<2:
            return False
        for i in s:
            if i in parentheses:
                stack.append(i)
            elif stack:
                if i!=parentheses[stack[-1]]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return len(stack)==0
