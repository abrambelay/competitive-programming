class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        res=0
        operations = {
            '+':lambda x,y:int(x)+int(y),
            '*':lambda x,y:int(x)*int(y),
            '-':lambda x,y:int(x)-int(y),
            '/':lambda x,y:int(int(x)/float(y))            
            }
        for i in tokens:
            if i in operations:
                if len(stack)>1:
                    res = operations[i](stack[-2],stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]
