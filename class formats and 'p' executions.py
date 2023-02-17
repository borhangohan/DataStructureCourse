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
    def clear(self):
        if self.isempty():
            print('empty')
        else:
            self.Data.clear()
    def printstack(self):
        if self.isempty():
            print('empty')
        else:
            print(self.Data)
        
object=stack()
print(object.Data)
object.peek()
object.push('a')
object.push('b')
object.push('c')
object.push('d')
object.push('e')
print(object.Data)
object.pop()
print(object.Data)
object.pop()
print(object.Data)
print(object.peek())
object.push('f')
object.push('g')
object.push('h')
print(object.Data)
object.pop()
print(object.Data)
print(object.size())
for char in tuple('ijklmn'):
    object.push(char)
object.printstack()
for i in list('wxyz'):
    object.push(i)
object.printstack()
print(object.size())
print(object.peek())




