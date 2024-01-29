class MyQueue(object):

    def __init__(self):
        self.s=[]
        

    def push(self, x):
        self.s.append(x)
        

    def pop(self):
        a=self.s[0]
        self.s=self.s[1:]
        return a
        

    def peek(self):
        return self.s[0]
        

    def empty(self):
        if len(self.s)>0:
            return 0
        return 1
        

