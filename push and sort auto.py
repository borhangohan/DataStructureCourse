class stack:
    def __init__(self):
        self.data=[]

    def size(self):
        return len(self.data)

    def push(self, data):
        self.data.append(data)
        

    def pop(self):
        if not stack:
            print('empty')
        else:
            return self.data.pop()

    def peek(self):
        if not stack:
            print('empty')
        else:
            return self.data[-1]

    def printstack(self):
        if not stack:
            print('empty')
        else:
            print(self.data.sort())

    def pushall(self, str):
        for ch in str:
            self.push(ch)
        ls=s.data
        ls.sort()
        return ls
        
    def pushStack(self,data):
        self.data.append(data)
        ls=self.data
        ls.sort()
        return ls

        
s=stack()
s.pushall([5,4,11,9,1,3,7])
print(s.data)
s.pushStack(2)
s.pushStack(10)
print(s.data)
