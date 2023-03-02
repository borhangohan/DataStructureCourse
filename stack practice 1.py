class stack:
  def __init__(self):
    self.data=[]
  def size(self):
    return len(self.data)

  def isEmpty(self):
    if self.size()==0:
      return True
    else:
      return False
  def push(self,data):
    if self.isEmpty():
        print('empty')
    else:
        self.data.append(data)
  def pop(self):
    if self.isEmpty():
        print('empty')
    else:
        return self.data.pop[-1]
  def sort(self):
    self.data.sort()
  def printstack(self):
    if self.size()==0:
      print('stack is empty.')
    else:
      print(self.data)
q=stack()
team_A=stack()
team_B=stack()
for i in list([2,4,7,10,1,9,11]):
    q.data.append(i)
q.printstack()  
q.sort()
q.printstack()
newlist=q.data
#2,4,7,10,1,9,11
while newlist:
    num=newlist.pop(0)
    if num%2==0:
        team_A.data.append(num)
    else:
        team_B.data.append(num)
# for num in newlist:
#     if num % 2 == 0:
#         team_A.data.pop(num)
#     else:
#         team_B.data.pop(num)
print('Team A:',team_A.data)
print('Team B:',team_B.data)