class stack:
    def __init__(self):
        self.Data=[]
    def size(self):
        return len(self.Data)
    def isempty(self):
        if self.size()==0:
            return True
        else:
            return False
    def push(self, data):
        self.Data.append(data)
    def pop(self):
        if not stack:
            print('empty')
        else:
            self.Data.pop()
    def peek(self):
        if self.isempty():
            print('empty')
        else:
            return self.Data[-1]
    def clearAll(self):
        if s.isempty():
            print('empty')     
        else:
            for i in range(s.size()):
                s.pop()   
s=stack()
s.push('a')
s.push('b')
s.push('c')
s.push('d')
print(s.Data)
s.clearAll()
s.peek()


