class MinStack(object):

    def __init__(self):
        self.stack=[]

    def push(self, val):
        self.stack.append(val)
        

    def pop(self):
        if len(self.stack)>0:
            self.stack.pop()

    def top(self):
        if len(self.stack)>0:
            return self.stack[-1]

    def getMin(self):
        if len(self.stack)>0:
            return min(self.stack)
        
