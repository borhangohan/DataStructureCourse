class stack:
    def __init__(self):
        self.data=[]

    def size(self):
        return len(self.data)

    def isempty(self):
        if self.size()==0:
            return True
        else:
            return False

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if self.isempty():
            print('empty')
        else:
            return self.data.pop()

    def peek(self):
        if self.isempty():
            print('empty')
        else:
            return self.data[-1]

    def printstack(self):
        if self.isempty():
            print('empty')
        else:
            print(self.data)

    def pushall(self, str):
        for ch in str:
            s.push(ch)

    def max(self):
        max_val= max(self.data)
        return max_val

    def keeplargestontop(self):
        max_val=s.max()
        for val in s.data:
            if val!=max_val:
                s1.data.append(val)
        s1.push(max_val)
        print(s1.data)
s=stack()
s1=stack()
s.printstack()
s.pushall([50, 40, 300, 20, 10])
s.printstack()
print(s.max())
s.keeplargestontop()


